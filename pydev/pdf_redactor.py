#!/usr/bin/env python3
"""
PDF PII Redactor - Local-only tool to redact PII from PDF files.

Reads PII values from a YAML config file and permanently redacts matching
text from PDFs using either black boxes or replacement text.

No network calls - runs entirely offline.
"""

import argparse
import os
import random
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
    samples: list = field(default_factory=list)
    sample_rate: float = 0.1  # Keep 1 in 10

    def add(self, record: RedactionRecord):
        self.total_redactions += 1
        self.counts_by_type[record.pii_type] = self.counts_by_type.get(record.pii_type, 0) + 1
        # Sample approximately 1 in 10
        if random.random() < self.sample_rate:
            self.samples.append(record)

    def merge(self, other: 'RedactionStats'):
        """Merge stats from another RedactionStats object."""
        self.total_redactions += other.total_redactions
        for pii_type, count in other.counts_by_type.items():
            self.counts_by_type[pii_type] = self.counts_by_type.get(pii_type, 0) + count
        self.samples.extend(other.samples)


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


def find_pattern_matches(page: fitz.Page, pattern: re.Pattern) -> list[tuple[fitz.Rect, str]]:
    """
    Find all regex pattern matches on a page and return their rectangles.

    Returns:
        List of (rectangle, matched_text) tuples
    """
    results = []
    page_text = page.get_text("text")

    # Find all matches of the pattern in the page text
    for match in pattern.finditer(page_text):
        matched_text = match.group()
        # Search for this exact text in the page to get its rectangle(s)
        rects = page.search_for(matched_text, flags=fitz.TEXT_PRESERVE_WHITESPACE)
        for rect in rects:
            results.append((rect, matched_text))

    return results


def find_and_redact(
    doc: fitz.Document,
    pii_list: list[PIIItem],
    mode: str = 'box',
    placeholder: str = '[REDACTED]',
    ignore_case: bool = False,
    verbose: bool = False,
    filename: str = ''
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

    Returns:
        RedactionStats with counts and samples
    """
    stats = RedactionStats()

    for page_num, page in enumerate(doc):
        for pii in pii_list:
            if pii.is_pattern:
                # Regex pattern matching
                matches = find_pattern_matches(page, pii.regex)
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
                        pii_type=f"pattern:{pii.value[:30]}",
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
                # Literal string matching
                flags = fitz.TEXT_PRESERVE_WHITESPACE
                text_instances = page.search_for(pii.value, flags=flags)

                if not text_instances:
                    continue

                if verbose:
                    print(f"  Page {page_num + 1}: Found {len(text_instances)} instance(s) of '{pii.value}'")

                # Add redaction annotations and track stats
                for rect in text_instances:
                    stats.add(RedactionRecord(
                        file=filename,
                        page=page_num + 1,
                        pii_type=pii.value[:30],
                        matched_text=pii.value
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
    verbose: bool
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
            filename=input_path.name
        )
        doc.save(output_path)
    finally:
        doc.close()
    return stats


def process_pdf_worker(args: tuple) -> tuple[str, RedactionStats | None, str | None]:
    """
    Worker function for parallel processing.

    Args:
        args: Tuple of (input_path, output_path, config_path, mode, placeholder, ignore_case, verbose)

    Returns:
        Tuple of (filename, RedactionStats, error_message_or_none)
    """
    input_path, output_path, config_path, mode, placeholder, ignore_case, verbose = args

    try:
        pii_list = load_config(config_path, ignore_case=ignore_case)
        stats = process_single_pdf(
            Path(input_path),
            Path(output_path),
            pii_list,
            mode=mode,
            placeholder=placeholder,
            ignore_case=ignore_case,
            verbose=verbose
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
                    args.verbose
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
                        verbose=args.verbose
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

        # Print breakdown by type
        if combined_stats.counts_by_type:
            print(f"\nRedactions by type:")
            for pii_type, count in sorted(combined_stats.counts_by_type.items(), key=lambda x: -x[1]):
                display = pii_type if len(pii_type) <= 40 else pii_type[:37] + "..."
                print(f"  {display}: {count}")

        # Print sample redactions
        if combined_stats.samples:
            print(f"\nSample redactions (~10% sampled, showing up to 20):")
            for sample in combined_stats.samples[:20]:
                matched_display = sample.matched_text if len(sample.matched_text) <= 30 else sample.matched_text[:27] + "..."
                print(f"  [{sample.file}:p{sample.page}] \"{matched_display}\"")

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
                verbose=args.verbose
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

        # Print breakdown by type
        if stats.counts_by_type:
            print(f"\nRedactions by type:")
            for pii_type, count in sorted(stats.counts_by_type.items(), key=lambda x: -x[1]):
                display = pii_type if len(pii_type) <= 40 else pii_type[:37] + "..."
                print(f"  {display}: {count}")

        # Print sample redactions
        if stats.samples:
            print(f"\nSample redactions (~10% sampled, showing up to 20):")
            for sample in stats.samples[:20]:
                matched_display = sample.matched_text if len(sample.matched_text) <= 30 else sample.matched_text[:27] + "..."
                print(f"  [p{sample.page}] \"{matched_display}\"")


if __name__ == '__main__':
    main()
