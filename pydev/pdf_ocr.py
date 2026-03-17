#!/usr/bin/env python3
"""
PDF OCR Test - Verify OCR text extraction works on scanned PDFs.

Detects scanned pages, runs OCR via Tesseract, and shows extracted text.
Use this to verify OCR quality before integrating with the redactor.

Note: PyMuPDF's get_textpage_ocr() extracts text in-memory but does not
embed a text layer into the PDF. For redaction of scanned PDFs, OCR
should be integrated directly into pdf_redactor.py.

Requires: Tesseract (brew install tesseract)
"""

import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF


def is_scanned_page(page: fitz.Page, min_chars: int = 10) -> bool:
    """Check if a page is likely scanned (has images but little/no text)."""
    text = page.get_text("text").strip()
    has_images = len(page.get_images()) > 0
    return has_images and len(text) < min_chars


def test_ocr(
    input_path: str,
    language: str = "eng",
    dpi: int = 300,
    force: bool = False,
    pages: list[int] | None = None
) -> dict:
    """
    Test OCR extraction on a PDF without modifying it.

    Args:
        input_path: Path to input PDF
        language: Tesseract language code
        dpi: Resolution for OCR (default 300, PyMuPDF default is 72 which is too low)
        force: OCR all pages, even those with existing text
        pages: Specific page numbers to test (1-based), or None for all

    Returns:
        Summary stats dict
    """
    doc = fitz.open(input_path)
    stats = {
        "total_pages": len(doc),
        "scanned_pages": 0,
        "ocr_pages": 0,
        "skipped_pages": 0,
        "page_results": {}
    }

    for page_num, page in enumerate(doc):
        page_display = page_num + 1

        # Skip if specific pages requested and this isn't one
        if pages and page_display not in pages:
            continue

        existing_text = page.get_text("text").strip()
        scanned = is_scanned_page(page)
        num_images = len(page.get_images())

        if scanned:
            stats["scanned_pages"] += 1

        if force or scanned:
            print(f"  Page {page_display}: Running OCR ({num_images} image(s), {len(existing_text)} existing chars)...")

            tp = page.get_textpage_ocr(language=language, dpi=dpi, full=True)
            ocr_text = page.get_text("text", textpage=tp).strip()

            stats["ocr_pages"] += 1
            stats["page_results"][page_display] = {
                "type": "ocr",
                "chars": len(ocr_text),
                "text": ocr_text
            }

            print(f"    Extracted {len(ocr_text)} chars via OCR")
        else:
            stats["skipped_pages"] += 1
            stats["page_results"][page_display] = {
                "type": "existing",
                "chars": len(existing_text),
                "text": existing_text
            }

            print(f"  Page {page_display}: Already has text ({len(existing_text)} chars, {num_images} image(s)), skipping OCR")

    doc.close()
    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Test OCR text extraction on scanned PDFs.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s scanned.pdf
  %(prog)s scanned.pdf --pages 1 3 5
  %(prog)s scanned.pdf --force
  %(prog)s scanned.pdf --full-text
        '''
    )

    parser.add_argument('input', help='Input PDF file')
    parser.add_argument(
        '-l', '--language',
        default='eng',
        help='Tesseract language code (default: eng)'
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='Resolution for OCR rendering (default: 300). Higher = better accuracy but slower'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='OCR all pages, even those with existing text'
    )
    parser.add_argument(
        '--pages',
        type=int,
        nargs='+',
        help='Specific page numbers to test (1-based)'
    )
    parser.add_argument(
        '--full-text',
        action='store_true',
        help='Show full extracted text (default: first 10 lines per page)'
    )

    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    print(f"Input: {args.input}")
    print(f"Language: {args.language}")
    print(f"DPI: {args.dpi}")
    print()

    try:
        stats = test_ocr(
            args.input,
            language=args.language,
            dpi=args.dpi,
            force=args.force,
            pages=args.pages
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Summary
    print(f"\n{'='*60}")
    print("OCR SUMMARY")
    print(f"{'='*60}")
    print(f"Total pages: {stats['total_pages']}")
    print(f"Scanned pages detected: {stats['scanned_pages']}")
    print(f"Pages OCR'd: {stats['ocr_pages']}")
    print(f"Pages skipped (already have text): {stats['skipped_pages']}")

    # Show extracted text
    if stats["page_results"]:
        print(f"\nExtracted text:")
        for page_num, result in stats["page_results"].items():
            source = "OCR" if result["type"] == "ocr" else "existing text layer"
            print(f"\n  --- Page {page_num} ({source}, {result['chars']} chars) ---")
            lines = result["text"].split('\n')
            if args.full_text:
                for line in lines:
                    print(f"  {line}")
            else:
                for line in lines[:10]:
                    print(f"  {line}")
                if len(lines) > 10:
                    print(f"  ... ({len(lines) - 10} more lines, use --full-text to see all)")


if __name__ == '__main__':
    main()
