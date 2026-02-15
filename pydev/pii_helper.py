#!/usr/bin/env python3
"""
PII Helper - Generate and add PII patterns to a YAML config file.

Supports:
  - Phone numbers (various formats)
  - SSN (last 4 digit matching)
  - Addresses (prefix matching)
  - Names (multiple variants)
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


def load_yaml(config_path: Path) -> dict:
    """Load existing YAML config or create empty structure."""
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}

    if 'pii' not in config:
        config['pii'] = {}

    return config


def save_yaml(config: dict, config_path: Path):
    """Save config to YAML file."""
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def add_to_section(config: dict, section: str, items: list):
    """Add items to a section, avoiding duplicates."""
    if section not in config['pii']:
        config['pii'][section] = []

    existing = config['pii'][section]
    for item in items:
        if item not in existing:
            existing.append(item)


def generate_phone_patterns(phone: str) -> list:
    """
    Generate regex patterns for a phone number.

    Input: 6505641234 or 650-564-1234 or (650) 564-1234
    Output: Patterns matching various phone formats
    """
    # Strip to just digits
    digits = re.sub(r'\D', '', phone)

    if len(digits) == 11 and digits.startswith('1'):
        # Remove leading country code
        digits = digits[1:]

    if len(digits) != 10:
        raise ValueError(f"Phone number must have 10 digits, got {len(digits)}: {phone}")

    area = digits[0:3]
    prefix = digits[3:6]
    line = digits[6:10]

    patterns = []

    # Plain digits
    patterns.append(digits)

    # Common formats as regex pattern
    # Matches: 650-564-1234, (650) 564-1234, 650.564.1234, 650 564 1234, +1 650-564-1234
    phone_pattern = (
        rf'(?:\+?1[-.\s]?)?'  # Optional country code
        rf'(?:\({area}\)|{area})[-.\s]?'  # Area code with optional parens
        rf'{prefix}[-.\s]?'  # Prefix
        rf'{line}'  # Line
    )
    patterns.append({'pattern': phone_pattern})

    return patterns


def generate_ssn_patterns(ssn: str) -> list:
    """
    Generate regex patterns for SSN with last 4 digits.

    Input: 123-45-6789 or 123456789
    Output: Patterns matching masked SSNs with same last 4
    """
    # Strip to just digits
    digits = re.sub(r'\D', '', ssn)

    if len(digits) != 9:
        raise ValueError(f"SSN must have 9 digits, got {len(digits)}: {ssn}")

    last4 = digits[5:9]

    patterns = []

    # Pattern for masked SSNs: XXX-XX-6789, ***-**-6789, etc.
    # Matches any combination of digits, X, x, *, # for first 5 digits
    masked_pattern = rf'[\dXx*#]{{3}}[-.\s]?[\dXx*#]{{2}}[-.\s]?{last4}'
    patterns.append({'pattern': masked_pattern})

    return patterns


def generate_address_patterns(address: str) -> list:
    """
    Generate regex patterns for an address prefix.

    Input: "123 Main St" or "456 Oak Avenue"
    Output: Patterns matching address with flexible spacing and abbreviations

    The street suffix (St, Rd, Ave, etc.) is made optional so "1234 S Main Rd"
    also matches "1234 S Main".
    """
    patterns = []

    # Literal match
    patterns.append(address)

    # Build flexible pattern
    # Split into parts and make spacing flexible
    parts = address.split()

    # Common street suffix expansions
    suffix_map = {
        'st': r'St(?:reet)?\.?',
        'street': r'St(?:reet)?\.?',
        'ave': r'Ave(?:nue)?\.?',
        'avenue': r'Ave(?:nue)?\.?',
        'rd': r'R(?:oa)?d\.?',
        'road': r'R(?:oa)?d\.?',
        'dr': r'Dr(?:ive)?\.?',
        'drive': r'Dr(?:ive)?\.?',
        'ln': r'L(?:a)?n(?:e)?\.?',
        'lane': r'L(?:a)?n(?:e)?\.?',
        'blvd': r'B(?:ou)?l(?:e)?v(?:ar)?d\.?',
        'boulevard': r'B(?:ou)?l(?:e)?v(?:ar)?d\.?',
        'ct': r'C(?:our)?t\.?',
        'court': r'C(?:our)?t\.?',
        'pl': r'Pl(?:ace)?\.?',
        'place': r'Pl(?:ace)?\.?',
        'cir': r'Cir(?:cle)?\.?',
        'circle': r'Cir(?:cle)?\.?',
        'way': r'Way',
        'apt': r'Apt\.?|Apartment',
        'apartment': r'Apt\.?|Apartment',
        'ste': r'Ste\.?|Suite',
        'suite': r'Ste\.?|Suite',
        '#': r'#|Apt\.?|Unit',
    }

    regex_parts = []
    for i, part in enumerate(parts):
        lower = part.lower().rstrip('.,')
        is_last = (i == len(parts) - 1)

        if lower in suffix_map:
            suffix_pattern = suffix_map[lower]
            if is_last:
                # Make trailing street suffix optional
                regex_parts.append(f'(?:\\s+{suffix_pattern})?')
            else:
                regex_parts.append(suffix_pattern)
        else:
            # Escape special regex characters
            regex_parts.append(re.escape(part))

    # Join with flexible whitespace (but suffix already has \s+ if optional)
    result_parts = []
    for i, part in enumerate(regex_parts):
        if part.startswith('(?:\\s+'):
            # Optional suffix already includes spacing
            result_parts.append(part)
        elif i == 0:
            result_parts.append(part)
        else:
            result_parts.append(r'\s+' + part)

    address_pattern = ''.join(result_parts)
    patterns.append({'pattern': address_pattern})

    return patterns


def generate_cc_patterns(cc_number: str) -> list:
    """
    Generate regex patterns for credit card with last 4 digits.

    Input: 1234567890123456 or 1234-5678-9012-3456
    Output: Patterns matching masked credit cards with same last 4
    """
    # Strip to just digits
    digits = re.sub(r'\D', '', cc_number)

    if len(digits) < 13 or len(digits) > 19:
        raise ValueError(f"Credit card must have 13-19 digits, got {len(digits)}: {cc_number}")

    last4 = digits[-4:]

    patterns = []

    # Exact match with common formats
    if len(digits) == 16:
        # Most common: 16 digits in groups of 4
        formatted = f"{digits[0:4]}-{digits[4:8]}-{digits[8:12]}-{digits[12:16]}"
        patterns.append(formatted)
        patterns.append(digits)  # Plain digits
    else:
        patterns.append(digits)

    # Pattern for masked credit cards: XXXX-XXXX-XXXX-3456, ****3456, etc.
    # Matches 12-15 masked characters followed by the last 4 digits
    # Supports X, x, *, #, or digits for masked portion, with optional separators
    masked_pattern = rf'[\dXx*#]{{4}}[-.\s]?[\dXx*#]{{4}}[-.\s]?[\dXx*#]{{4}}[-.\s]?{last4}'
    patterns.append({'pattern': masked_pattern})

    # Also match shorter format without separators (just masked + last 4)
    # e.g., ************3456 or XXXXXXXXXXXX3456
    short_masked = rf'[\dXx*#]{{12,15}}{last4}'
    patterns.append({'pattern': short_masked})

    return patterns


def generate_name_variants(first_name: str, last_name: str) -> list:
    """
    Generate name variants for matching.

    Input: "John", "Smith"
    Output: Various name formats as literal strings
    """
    variants = []

    first = first_name.strip()
    last = last_name.strip()
    first_initial = first[0] if first else ''
    last_initial = last[0] if last else ''

    # Full name variants
    variants.append(f"{first} {last}")  # John Smith
    variants.append(f"{last}, {first}")  # Smith, John
    variants.append(f"{first_initial}. {last}")  # J. Smith
    variants.append(f"{last}, {first_initial}.")  # Smith, J.
    variants.append(f"{first_initial} {last}")  # J Smith

    # Case variants as patterns
    # Matches case-insensitive full name
    name_pattern = rf'(?i){re.escape(first)}\s+{re.escape(last)}'
    variants.append({'pattern': name_pattern})

    # Last, First pattern (case-insensitive)
    reverse_pattern = rf'(?i){re.escape(last)},?\s+{re.escape(first)}'
    variants.append({'pattern': reverse_pattern})

    return variants


def cmd_phone(args):
    """Handle phone number command."""
    config = load_yaml(args.config)

    for phone in args.numbers:
        try:
            patterns = generate_phone_patterns(phone)
            add_to_section(config, 'phones', patterns)
            print(f"Added phone patterns for: {phone}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_ssn(args):
    """Handle SSN command."""
    config = load_yaml(args.config)

    for ssn in args.ssns:
        try:
            patterns = generate_ssn_patterns(ssn)
            add_to_section(config, 'ssn', patterns)
            print(f"Added SSN patterns for last 4: ***-**-{ssn[-4:]}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_address(args):
    """Handle address command."""
    config = load_yaml(args.config)

    for address in args.addresses:
        patterns = generate_address_patterns(address)
        add_to_section(config, 'addresses', patterns)
        print(f"Added address patterns for: {address}")

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_cc(args):
    """Handle credit card command."""
    config = load_yaml(args.config)

    for cc in args.cards:
        try:
            patterns = generate_cc_patterns(cc)
            add_to_section(config, 'credit_cards', patterns)
            last4 = re.sub(r'\D', '', cc)[-4:]
            print(f"Added credit card patterns for last 4: ****{last4}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_name(args):
    """Handle name command."""
    config = load_yaml(args.config)

    for name in args.names:
        parts = name.split(maxsplit=1)
        if len(parts) != 2:
            print(f"Error: Name must be 'FirstName LastName', got: {name}", file=sys.stderr)
            return 1

        first, last = parts
        variants = generate_name_variants(first, last)
        add_to_section(config, 'names', variants)
        print(f"Added name variants for: {first} {last}")

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_show(args):
    """Show current config contents."""
    config = load_yaml(args.config)
    print(yaml.dump(config, default_flow_style=False, allow_unicode=True, sort_keys=False))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Generate and add PII patterns to a YAML config file.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s phone -c pii.yaml 6505641234
  %(prog)s ssn -c pii.yaml 123-45-6789
  %(prog)s cc -c pii.yaml 4111111111111234
  %(prog)s address -c pii.yaml "123 Main Street"
  %(prog)s name -c pii.yaml "John Smith"
  %(prog)s show -c pii.yaml
        '''
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Phone command
    phone_parser = subparsers.add_parser('phone', help='Add phone number patterns')
    phone_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    phone_parser.add_argument('numbers', nargs='+', help='Phone numbers to add')
    phone_parser.set_defaults(func=cmd_phone)

    # SSN command
    ssn_parser = subparsers.add_parser('ssn', help='Add SSN patterns (matches masked versions with same last 4)')
    ssn_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    ssn_parser.add_argument('ssns', nargs='+', help='SSNs to add')
    ssn_parser.set_defaults(func=cmd_ssn)

    # Address command
    addr_parser = subparsers.add_parser('address', help='Add address patterns')
    addr_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    addr_parser.add_argument('addresses', nargs='+', help='Address prefixes to add')
    addr_parser.set_defaults(func=cmd_address)

    # Credit card command
    cc_parser = subparsers.add_parser('cc', help='Add credit card patterns (matches masked versions with same last 4)')
    cc_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    cc_parser.add_argument('cards', nargs='+', help='Credit card numbers to add')
    cc_parser.set_defaults(func=cmd_cc)

    # Name command
    name_parser = subparsers.add_parser('name', help='Add name variants')
    name_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    name_parser.add_argument('names', nargs='+', help='Names as "FirstName LastName"')
    name_parser.set_defaults(func=cmd_name)

    # Show command
    show_parser = subparsers.add_parser('show', help='Show current config')
    show_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    show_parser.set_defaults(func=cmd_show)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == '__main__':
    main()
