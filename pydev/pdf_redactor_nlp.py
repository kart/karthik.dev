#!/usr/bin/env python3
"""
PDF PII Redactor (NLP) - Automatically detect and redact PII using NLP.

Uses Microsoft Presidio for comprehensive PII detection, with optional
spaCy-only mode for lighter-weight processing.

No internet required - runs entirely offline using local models.
"""

import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF

# Lazy imports for NLP libraries
presidio_available = False
spacy_available = False


def check_presidio():
    """Check if Presidio is available."""
    global presidio_available
    try:
        from presidio_analyzer import AnalyzerEngine
        presidio_available = True
        return True
    except ImportError:
        return False


def check_spacy():
    """Check if spaCy is available."""
    global spacy_available
    try:
        import spacy
        spacy_available = True
        return True
    except ImportError:
        return False


def get_presidio_analyzer():
    """Initialize and return Presidio analyzer."""
    from presidio_analyzer import AnalyzerEngine
    from presidio_analyzer.nlp_engine import NlpEngineProvider

    # Configure to use spaCy
    provider = NlpEngineProvider(nlp_configuration={
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}]
    })
    nlp_engine = provider.create_engine()
    return AnalyzerEngine(nlp_engine=nlp_engine)


def detect_pii_presidio(text: str, analyzer, entities: list[str] | None = None) -> list[dict]:
    """
    Detect PII using Presidio.

    Returns list of dicts with 'text', 'type', 'start', 'end', 'score'.
    """
    # Default entities to detect
    if entities is None:
        entities = [
            "PERSON",
            "EMAIL_ADDRESS",
            "PHONE_NUMBER",
            "US_SSN",
            "CREDIT_CARD",
            "US_PASSPORT",
            "US_DRIVER_LICENSE",
            "IP_ADDRESS",
            "IBAN_CODE",
            "US_BANK_NUMBER",
            "LOCATION",
            "DATE_TIME",
        ]

    results = analyzer.analyze(text=text, language="en", entities=entities)

    pii_found = []
    for result in results:
        pii_found.append({
            "text": text[result.start:result.end],
            "type": result.entity_type,
            "start": result.start,
            "end": result.end,
            "score": result.score
        })

    return pii_found


def detect_pii_spacy(text: str, nlp) -> list[dict]:
    """
    Detect PII using spaCy NER only.

    Detects: PERSON, ORG, GPE (locations), DATE, etc.
    Also uses regex patterns for emails, phones, SSNs.
    """
    import re

    pii_found = []

    # spaCy NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC", "DATE", "MONEY", "CARDINAL"]:
            pii_found.append({
                "text": ent.text,
                "type": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
                "score": 0.85
            })

    # Regex patterns for common PII
    patterns = {
        "EMAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "PHONE": r'\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b',
        "SSN": r'\b\d{3}-\d{2}-\d{4}\b',
        "CREDIT_CARD": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        "IP_ADDRESS": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    }

    for pii_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            pii_found.append({
                "text": match.group(),
                "type": pii_type,
                "start": match.start(),
                "end": match.end(),
                "score": 0.95
            })

    return pii_found


def extract_text_with_positions(page) -> list[dict]:
    """
    Extract text blocks with their positions from a PDF page.

    Returns list of dicts with 'text', 'rect'.
    """
    blocks = page.get_text("dict")["blocks"]
    text_items = []

    for block in blocks:
        if "lines" in block:
            for line in block["lines"]:
                for span in line["spans"]:
                    text_items.append({
                        "text": span["text"],
                        "rect": fitz.Rect(span["bbox"])
                    })

    return text_items


def find_pii_locations(page, pii_texts: list[str]) -> list[tuple[fitz.Rect, str]]:
    """
    Find locations of PII text on the page.

    Returns list of (rect, pii_text) tuples.
    """
    locations = []
    for pii in pii_texts:
        rects = page.search_for(pii)
        for rect in rects:
            locations.append((rect, pii))
    return locations


def redact_page(
    page,
    pii_locations: list[tuple[fitz.Rect, str]],
    mode: str = 'box',
    placeholder: str = '[REDACTED]'
):
    """Apply redactions to a page."""
    for rect, pii_text in pii_locations:
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

    page.apply_redactions()


def process_pdf(
    input_path: str,
    output_path: str,
    mode: str = 'box',
    placeholder: str = '[REDACTED]',
    use_presidio: bool = True,
    min_score: float = 0.5,
    verbose: bool = False
) -> dict:
    """
    Process a PDF, detect PII, and redact it.

    Returns summary statistics.
    """
    # Initialize NLP engine
    if use_presidio:
        if not check_presidio():
            raise ImportError("Presidio not installed. Run: pip install presidio-analyzer presidio-anonymizer")
        analyzer = get_presidio_analyzer()
        if verbose:
            print("Using Presidio for PII detection")
    else:
        if not check_spacy():
            raise ImportError("spaCy not installed. Run: pip install spacy && python -m spacy download en_core_web_sm")
        import spacy
        nlp = spacy.load("en_core_web_sm")
        if verbose:
            print("Using spaCy-only for PII detection")

    doc = fitz.open(input_path)
    stats = {"pages": len(doc), "pii_found": [], "redactions": 0}

    for page_num, page in enumerate(doc):
        # Extract full page text
        page_text = page.get_text()

        # Detect PII
        if use_presidio:
            pii_items = detect_pii_presidio(page_text, analyzer)
        else:
            pii_items = detect_pii_spacy(page_text, nlp)

        # Filter by confidence score
        pii_items = [p for p in pii_items if p["score"] >= min_score]

        if not pii_items:
            continue

        # Get unique PII texts
        pii_texts = list(set(p["text"] for p in pii_items))

        # Find locations on page
        pii_locations = find_pii_locations(page, pii_texts)

        if verbose and pii_locations:
            print(f"  Page {page_num + 1}:")
            for _, pii_text in pii_locations:
                pii_type = next((p["type"] for p in pii_items if p["text"] == pii_text), "UNKNOWN")
                print(f"    [{pii_type}] {pii_text[:40]}{'...' if len(pii_text) > 40 else ''}")

        # Apply redactions
        redact_page(page, pii_locations, mode, placeholder)

        stats["pii_found"].extend(pii_items)
        stats["redactions"] += len(pii_locations)

    doc.save(output_path)
    doc.close()

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Automatically detect and redact PII from PDFs using NLP.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s input.pdf -o output.pdf
  %(prog)s input.pdf -o output.pdf --spacy-only
  %(prog)s input.pdf -o output.pdf --mode replace --placeholder "[REMOVED]"
  %(prog)s input.pdf -o output.pdf --min-score 0.7 -v
        '''
    )

    parser.add_argument('input', help='Input PDF file')
    parser.add_argument('-o', '--output', required=True, help='Output PDF file')
    parser.add_argument(
        '-m', '--mode',
        choices=['box', 'replace'],
        default='box',
        help='Redaction mode (default: box)'
    )
    parser.add_argument(
        '-p', '--placeholder',
        default='[REDACTED]',
        help='Replacement text for replace mode (default: [REDACTED])'
    )
    parser.add_argument(
        '--spacy-only',
        action='store_true',
        help='Use spaCy NER only (lighter, but less comprehensive)'
    )
    parser.add_argument(
        '--min-score',
        type=float,
        default=0.5,
        help='Minimum confidence score for PII detection (0.0-1.0, default: 0.5)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed detection information'
    )

    args = parser.parse_args()

    # Validate input
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"Processing: {args.input}")
        print(f"Mode: {args.mode}")
        print(f"Min confidence: {args.min_score}")

    try:
        stats = process_pdf(
            args.input,
            args.output,
            mode=args.mode,
            placeholder=args.placeholder,
            use_presidio=not args.spacy_only,
            min_score=args.min_score,
            verbose=args.verbose
        )
    except ImportError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing PDF: {e}", file=sys.stderr)
        sys.exit(1)

    # Summary
    print(f"\nProcessed {stats['pages']} page(s)")
    print(f"PII detected: {len(stats['pii_found'])} item(s)")
    print(f"Redactions applied: {stats['redactions']}")

    if args.verbose and stats['pii_found']:
        # Group by type
        by_type = {}
        for p in stats['pii_found']:
            by_type[p['type']] = by_type.get(p['type'], 0) + 1
        print("\nPII by type:")
        for pii_type, count in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {pii_type}: {count}")

    print(f"\nOutput saved to: {args.output}")


if __name__ == '__main__':
    main()
