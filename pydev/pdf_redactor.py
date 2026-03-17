#!/usr/bin/env python3
"""
PDF PII Redactor - Local-only tool to redact PII from PDF files.

Reads PII values from a YAML config file and permanently redacts matching
text from PDFs using either black boxes or replacement text.

No network calls - runs entirely offline.
"""

import argparse
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from dataclasses import dataclass, field

import fitz  # PyMuPDF
import yaml


@dataclass
class RedactionRecord:
    """Record of a single redaction."""
    file: str
    page: int
    pii_type: str  # The pattern or literal that matched
    matched_text: str  # The actual text that was redacted


@dataclass
class RedactionStats:
    """Statistics and samples from redaction processing."""
    total_redactions: int = 0
    counts_by_type: dict = field(default_factory=dict)
    # matched_texts_by_type: pii_type -> {matched_text: count}
    matched_texts_by_type: dict = field(default_factory=dict)

    def add(self, record: RedactionRecord):
        self.total_redactions += 1
        self.counts_by_type[record.pii_type] = self.counts_by_type.get(record.pii_type, 0) + 1
        if record.pii_type not in self.matched_texts_by_type:
            self.matched_texts_by_type[record.pii_type] = {}
        texts = self.matched_texts_by_type[record.pii_type]
        texts[record.matched_text] = texts.get(record.matched_text, 0) + 1

    def merge(self, other: 'RedactionStats'):
        """Merge stats from another RedactionStats object."""
        self.total_redactions += other.total_redactions
        for pii_type, count in other.counts_by_type.items():
            self.counts_by_type[pii_type] = self.counts_by_type.get(pii_type, 0) + count
        for pii_type, texts in other.matched_texts_by_type.items():
            if pii_type not in self.matched_texts_by_type:
                self.matched_texts_by_type[pii_type] = {}
            for text, count in texts.items():
                self.matched_texts_by_type[pii_type][text] = self.matched_texts_by_type[pii_type].get(text, 0) + count


@dataclass
class PIIItem:
    """Represents a PII item to search for - either literal text or a regex pattern."""
    value: str
    is_pattern: bool = False
    regex: re.Pattern = None

    def __post_init__(self):
        if self.is_pattern and self.regex is None:
            self.regex = re.compile(self.value, re.IGNORECASE)


def load_config(config_path: str, ignore_case: bool = False) -> list[PIIItem]:
    r"""
    Load PII values from YAML config file.

    Supports both literal strings and regex patterns:
        pii:
          names:
            - John Smith
          ssn_last4:
            - pattern: '[\dXx*#]{3}-[\dXx*#]{2}-1234'

    Returns a list of PIIItem objects.
    """
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    if not config or 'pii' not in config:
        raise ValueError("Config file must contain a 'pii' section")

    # Flatten all PII values into a single list
    pii_items = []
    flags = re.IGNORECASE if ignore_case else 0

    for category, values in config['pii'].items():
        if not values:
            continue
        if not isinstance(values, list):
            values = [values]

        for v in values:
            if not v:
                continue
            if isinstance(v, dict) and 'pattern' in v:
                # Regex pattern
                try:
                    regex = re.compile(v['pattern'], flags)
                    pii_items.append(PIIItem(
                        value=v['pattern'],
                        is_pattern=True,
                        regex=regex
                    ))
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern '{v['pattern']}': {e}")
            else:
                # Literal string
                pii_items.append(PIIItem(value=str(v), is_pattern=False))

    return pii_items


def is_scanned_page(page: fitz.Page, min_chars: int = 10) -> bool:
    """Check if a page is likely scanned (has images but little/no text)."""
    text = page.get_text("text").strip()
    has_images = len(page.get_images()) > 0
    return has_images and len(text) < min_chars


def find_pattern_matches(
    page: fitz.Page,
    pattern: re.Pattern,
    textpage: object = None
) -> list[tuple[fitz.Rect, str]]:
    """
    Find all regex pattern matches on a page and return their rectangles.

    Uses regex to find matches in the page text, then locates each match
    on the page. Since PyMuPDF's search_for is case-insensitive, we verify
    each candidate rectangle's actual text against the regex pattern.

    Args:
        page: PyMuPDF page object
        pattern: Compiled regex pattern
        textpage: Optional TextPage from OCR (for scanned pages)

    Returns:
        List of (rectangle, matched_text) tuples
    """
    results = []
    page_text = page.get_text("text", textpage=textpage)
    # Get all words with positions for context verification.
    # Each word: (x0, y0, x1, y1, "word", block_no, line_no, word_no)
    words = page.get_text("words", textpage=textpage)

    # Find all matches of the pattern in the page text
    for match in pattern.finditer(page_text):
        matched_text = match.group()
        # search_for is always case-insensitive, so it may return extra rects.
        # For each candidate rect, find the overlapping word(s) and verify
        # the pattern against the full word context so that word boundaries
        # like \b are evaluated correctly.
        rects = page.search_for(matched_text, flags=fitz.TEXT_PRESERVE_WHITESPACE, textpage=textpage)
        for rect in rects:
            overlapping = [w[4] for w in words if fitz.Rect(w[:4]).intersects(rect)]
            context = " ".join(overlapping) if overlapping else ""
            if not pattern.search(context):
                continue
            results.append((rect, matched_text))

    return results


def find_and_redact(
    doc: fitz.Document,
    pii_list: list[PIIItem],
    mode: str = 'box',
    placeholder: str = '[REDACTED]',
    ignore_case: bool = False,
    verbose: bool = False,
    filename: str = '',
    ocr: bool = False,
    ocr_dpi: int = 300,
    ocr_language: str = 'eng'
) -> RedactionStats:
    """
    Find and redact all PII occurrences in the document.

    Args:
        doc: PyMuPDF document object
        pii_list: List of PIIItem objects to search for
        mode: 'box' for black boxes, 'replace' for replacement text
        placeholder: Text to use in replace mode
        ignore_case: Whether to ignore case when matching (for literal strings)
        verbose: Print details about what was redacted
        filename: Name of the file being processed (for stats)
        ocr: Whether to use OCR for scanned pages
        ocr_dpi: Resolution for OCR rendering
        ocr_language: Tesseract language code

    Returns:
        RedactionStats with counts and samples
    """
    stats = RedactionStats()

    for page_num, page in enumerate(doc):
        # Determine if this page needs OCR
        textpage = None
        if ocr and is_scanned_page(page):
            if verbose:
                print(f"  Page {page_num + 1}: Scanned page detected, running OCR (dpi={ocr_dpi})...")
            textpage = page.get_textpage_ocr(
                language=ocr_language, dpi=ocr_dpi, full=True
            )

        for pii in pii_list:
            if pii.is_pattern:
                # Regex pattern matching
                matches = find_pattern_matches(page, pii.regex, textpage=textpage)
                if not matches:
                    continue

                if verbose:
                    matched_texts = set(m[1] for m in matches)
                    print(f"  Page {page_num + 1}: Pattern '{pii.value}' matched {len(matches)} instance(s): {matched_texts}")

                # Add redaction annotations and track stats
                for rect, matched_text in matches:
                    stats.add(RedactionRecord(
                        file=filename,
                        page=page_num + 1,
                        pii_type=f"pattern:{pii.value}",
                        matched_text=matched_text
                    ))
                    if mode == 'replace':
                        page.add_redact_annot(
                            rect,
                            text=placeholder,
                            fill=(1, 1, 1),
                            text_color=(0, 0, 0),
                            fontsize=10
                        )
                    else:
                        page.add_redact_annot(rect, fill=(0, 0, 0))
            else:
                # Literal string matching with word boundaries
                literal_pattern = re.compile(
                    r'\b' + re.escape(pii.value) + r'\b',
                    re.IGNORECASE if ignore_case else 0
                )
                matches = find_pattern_matches(page, literal_pattern, textpage=textpage)

                if not matches:
                    continue

                if verbose:
                    print(f"  Page {page_num + 1}: Found {len(matches)} instance(s) of '{pii.value}'")

                # Add redaction annotations and track stats
                for rect, matched_text in matches:
                    stats.add(RedactionRecord(
                        file=filename,
                        page=page_num + 1,
                        pii_type=pii.value,
                        matched_text=matched_text
                    ))
                    if mode == 'replace':
                        page.add_redact_annot(
                            rect,
                            text=placeholder,
                            fill=(1, 1, 1),
                            text_color=(0, 0, 0),
                            fontsize=10
                        )
                    else:
                        page.add_redact_annot(rect, fill=(0, 0, 0))

        # Apply all redactions for this page
        page.apply_redactions()

    return stats


def process_single_pdf(
    input_path: Path,
    output_path: Path,
    pii_list: list[PIIItem],
    mode: str,
    placeholder: str,
    ignore_case: bool,
    verbose: bool,
    ocr: bool = False,
    ocr_dpi: int = 300,
    ocr_language: str = 'eng'
) -> RedactionStats:
    """
    Process a single PDF file and save the redacted version.

    Returns:
        RedactionStats with counts and samples
    """
    doc = fitz.open(input_path)
    try:
        stats = find_and_redact(
            doc,
            pii_list,
            mode=mode,
            placeholder=placeholder,
            ignore_case=ignore_case,
            verbose=verbose,
            filename=input_path.name,
            ocr=ocr,
            ocr_dpi=ocr_dpi,
            ocr_language=ocr_language
        )
        doc.save(output_path)
    finally:
        doc.close()
    return stats


def process_pdf_worker(args: tuple) -> tuple[str, RedactionStats | None, str | None]:
    """
    Worker function for parallel processing.

    Args:
        args: Tuple of (input_path, output_path, config_path, mode, placeholder,
              ignore_case, verbose, ocr, ocr_dpi, ocr_language)

    Returns:
        Tuple of (filename, RedactionStats, error_message_or_none)
    """
    input_path, output_path, config_path, mode, placeholder, ignore_case, verbose, ocr, ocr_dpi, ocr_language = args

    try:
        pii_list = load_config(config_path, ignore_case=ignore_case)
        stats = process_single_pdf(
            Path(input_path),
            Path(output_path),
            pii_list,
            mode=mode,
            placeholder=placeholder,
            ignore_case=ignore_case,
            verbose=verbose,
            ocr=ocr,
            ocr_dpi=ocr_dpi,
            ocr_language=ocr_language
        )
        return (Path(input_path).name, stats, None)
    except Exception as e:
        return (Path(input_path).name, None, str(e))


def main():
    parser = argparse.ArgumentParser(
        description='Redact PII from PDF files using values from a YAML config.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Single file mode
  %(prog)s input.pdf --config pii.yaml -o output.pdf
  %(prog)s input.pdf --config pii.yaml -o output.pdf --mode replace
  %(prog)s input.pdf --config pii.yaml -o output.pdf --mode replace --placeholder "[REMOVED]"
  %(prog)s input.pdf --config pii.yaml -o output.pdf -v --ignore-case

  # Directory mode (outputs to <directory>/redacted/)
  %(prog)s --directory ./pdfs --config pii.yaml
  %(prog)s -d ./pdfs -c pii.yaml --mode replace -v
  %(prog)s -d ./pdfs -c pii.yaml --workers 4  # parallel processing

Config file format (supports literal strings and regex patterns):
  pii:
    names:
      - John Smith
      - Jane Doe
    ssn_last4:
      - pattern: '[\\dXx*#]{3}-[\\dXx*#]{2}-1234'
      - pattern: '[\\dXx*#]{3}-[\\dXx*#]{2}-5678'
    emails:
      - pattern: 'john\\.smith@[a-z]+\\.com'
        '''
    )

    parser.add_argument(
        'input',
        nargs='?',
        help='Input PDF file to redact (not used with --directory)'
    )
    parser.add_argument(
        '-d', '--directory',
        help='Directory containing PDF files to redact (outputs to <directory>/redacted/)'
    )
    parser.add_argument(
        '-c', '--config',
        required=True,
        help='YAML config file containing PII values to redact'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output PDF file path (not used with --directory)'
    )
    parser.add_argument(
        '-m', '--mode',
        choices=['box', 'replace'],
        default='box',
        help='Redaction mode: "box" for black boxes (default), "replace" for text replacement'
    )
    parser.add_argument(
        '-p', '--placeholder',
        default='[REDACTED]',
        help='Replacement text when using --mode replace (default: [REDACTED])'
    )
    parser.add_argument(
        '-i', '--ignore-case',
        action='store_true',
        help='Ignore case when matching PII values'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed information about redactions'
    )
    parser.add_argument(
        '-w', '--workers',
        type=int,
        default=1,
        help='Number of parallel workers for directory mode (default: 1)'
    )
    parser.add_argument(
        '--ocr',
        action='store_true',
        help='Use OCR for scanned pages (requires Tesseract)'
    )
    parser.add_argument(
        '--ocr-dpi',
        type=int,
        default=300,
        help='Resolution for OCR rendering (default: 300)'
    )
    parser.add_argument(
        '--ocr-language',
        default='eng',
        help='Tesseract language code for OCR (default: eng)'
    )

    args = parser.parse_args()

    # Validate arguments based on mode
    if args.directory:
        dir_path = Path(args.directory)
        if not dir_path.is_dir():
            print(f"Error: Directory not found: {args.directory}", file=sys.stderr)
            sys.exit(1)
    else:
        if not args.input:
            print("Error: Either provide an input file or use --directory", file=sys.stderr)
            sys.exit(1)
        if not args.output:
            print("Error: --output is required when processing a single file", file=sys.stderr)
            sys.exit(1)
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)

    # Load PII config
    try:
        pii_list = load_config(args.config, ignore_case=args.ignore_case)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not pii_list:
        print("Warning: No PII values found in config file", file=sys.stderr)
        sys.exit(0)

    if args.verbose:
        literal_count = sum(1 for p in pii_list if not p.is_pattern)
        pattern_count = sum(1 for p in pii_list if p.is_pattern)
        print(f"Loaded {len(pii_list)} PII item(s) from config ({literal_count} literal, {pattern_count} pattern)")
        print(f"Mode: {args.mode}")

    # Directory mode
    if args.directory:
        dir_path = Path(args.directory)
        output_dir = dir_path / "redacted"
        output_dir.mkdir(exist_ok=True)

        pdf_files = list(dir_path.glob("*.pdf")) + list(dir_path.glob("*.PDF"))
        if not pdf_files:
            print(f"No PDF files found in {args.directory}", file=sys.stderr)
            sys.exit(0)

        if args.verbose:
            print(f"Found {len(pdf_files)} PDF file(s) in {args.directory}")
            print(f"Output directory: {output_dir}")
            if args.workers > 1:
                print(f"Using {args.workers} parallel workers")

        total_files = 0
        failed_files = []
        combined_stats = RedactionStats()

        if args.workers > 1:
            # Parallel processing
            worker_args = [
                (
                    str(pdf_path),
                    str(output_dir / pdf_path.name),
                    args.config,
                    args.mode,
                    args.placeholder,
                    args.ignore_case,
                    args.verbose,
                    args.ocr,
                    args.ocr_dpi,
                    args.ocr_language
                )
                for pdf_path in pdf_files
            ]

            with ProcessPoolExecutor(max_workers=args.workers) as executor:
                futures = {executor.submit(process_pdf_worker, arg): arg[0] for arg in worker_args}

                for future in as_completed(futures):
                    filename, stats, error = future.result()
                    if error:
                        print(f"Error processing {filename}: {error}", file=sys.stderr)
                        failed_files.append(filename)
                    else:
                        combined_stats.merge(stats)
                        total_files += 1
                        if args.verbose:
                            print(f"  {filename}: {stats.total_redactions} redaction(s)")
        else:
            # Sequential processing
            for pdf_path in pdf_files:
                output_path = output_dir / pdf_path.name
                if args.verbose:
                    print(f"\nProcessing: {pdf_path.name}")

                try:
                    stats = process_single_pdf(
                        pdf_path,
                        output_path,
                        pii_list,
                        mode=args.mode,
                        placeholder=args.placeholder,
                        ignore_case=args.ignore_case,
                        verbose=args.verbose,
                        ocr=args.ocr,
                        ocr_dpi=args.ocr_dpi,
                        ocr_language=args.ocr_language
                    )
                    combined_stats.merge(stats)
                    total_files += 1
                    if args.verbose:
                        print(f"  -> {stats.total_redactions} redaction(s), saved to {output_path.name}")
                except Exception as e:
                    print(f"Error processing {pdf_path.name}: {e}", file=sys.stderr)
                    failed_files.append(pdf_path.name)

        # Print summary
        print(f"\n{'='*60}")
        print("REDACTION SUMMARY")
        print(f"{'='*60}")
        print(f"Files processed: {total_files}/{len(pdf_files)}")
        print(f"Total redactions: {combined_stats.total_redactions}")
        print(f"Output directory: {output_dir}")
        if failed_files:
            print(f"Failed files: {', '.join(failed_files)}")

        # Print breakdown by type with matched texts
        if combined_stats.counts_by_type:
            print(f"\nRedactions by type:")
            for pii_type, count in sorted(combined_stats.counts_by_type.items(), key=lambda x: -x[1]):
                print(f"  {pii_type}: {count}")
                texts = combined_stats.matched_texts_by_type.get(pii_type, {})
                for text, text_count in sorted(texts.items(), key=lambda x: -x[1]):
                    print(f"    \"{text}\" x{text_count}")

    # Single file mode
    else:
        input_path = Path(args.input)
        output_path = Path(args.output)

        if args.verbose:
            print(f"Processing: {args.input}")

        try:
            stats = process_single_pdf(
                input_path,
                output_path,
                pii_list,
                mode=args.mode,
                placeholder=args.placeholder,
                ignore_case=args.ignore_case,
                verbose=args.verbose,
                ocr=args.ocr,
                ocr_dpi=args.ocr_dpi,
                ocr_language=args.ocr_language
            )
        except Exception as e:
            print(f"Error processing PDF: {e}", file=sys.stderr)
            sys.exit(1)

        # Print summary
        print(f"\n{'='*60}")
        print("REDACTION SUMMARY")
        print(f"{'='*60}")
        print(f"Total redactions: {stats.total_redactions}")
        print(f"Output saved to: {args.output}")

        # Print breakdown by type with matched texts
        if stats.counts_by_type:
            print(f"\nRedactions by type:")
            for pii_type, count in sorted(stats.counts_by_type.items(), key=lambda x: -x[1]):
                print(f"  {pii_type}: {count}")
                texts = stats.matched_texts_by_type.get(pii_type, {})
                for text, text_count in sorted(texts.items(), key=lambda x: -x[1]):
                    print(f"    \"{text}\" x{text_count}")


if __name__ == '__main__':
    main()
