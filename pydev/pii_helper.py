#!/usr/bin/env python3
"""
PII Helper - Generate and add PII patterns to a YAML config file.

Supports:
  - Phone numbers (various formats)
  - SSN (last 4 digit matching)
  - Addresses (component-based: street, city, state, zip)
  - Names (component-based: first/last with individual + combined variants)
  - Email addresses (component-based: user/domain with obfuscated forms)
  - Dates of birth (component-based: month/day/year with all format variants)
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


def generate_ssn_patterns(last4: str) -> list:
    """
    Generate regex patterns for SSN with last 4 digits.

    Input: "6789"
    Output: Patterns matching masked SSNs with same last 4
    """
    digits = re.sub(r'\D', '', last4)

    if len(digits) != 4:
        raise ValueError(f"SSN last 4 must have exactly 4 digits, got {len(digits)}: {last4}")

    patterns = []

    # Pattern for masked SSNs: XXX-XX-6789, ***-**-6789, etc.
    # Matches any combination of digits, X, x, *, # for first 5 digits
    masked_pattern = rf'[\dXx*#]{{3}}[-.\s]?[\dXx*#]{{2}}[-.\s]?{digits}'
    patterns.append({'pattern': masked_pattern})

    return patterns


def _build_street_pattern(street: str) -> str:
    """
    Build a flexible regex pattern for a street string.

    Handles abbreviation expansion (St/Street, Ave/Avenue, etc.)
    and makes the trailing suffix optional.
    """
    parts = street.split()

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
                regex_parts.append(f'(?:\\s+{suffix_pattern})?')
            else:
                regex_parts.append(suffix_pattern)
        else:
            regex_parts.append(re.escape(part))

    result_parts = []
    for i, part in enumerate(regex_parts):
        if part.startswith('(?:\\s+'):
            result_parts.append(part)
        elif i == 0:
            result_parts.append(part)
        else:
            result_parts.append(r'\s+' + part)

    return ''.join(result_parts)


def generate_address_patterns(
    street: str,
    city: str | None = None,
    state: str | None = None,
    zipcode: str | None = None
) -> list:
    """
    Generate patterns for address components and their combinations.

    Each component is added as a standalone literal, plus regex patterns
    for common multi-component combinations (street+city, city+state, etc.)
    and full address with flexible separators.
    """
    patterns = []

    # Individual components as literals
    patterns.append(street)
    if city:
        patterns.append(city)
    if state and len(state) > 2:
        patterns.append(state)
    if zipcode:
        patterns.append(zipcode)

    # Street with flexible suffix abbreviations
    street_pat = _build_street_pattern(street)
    patterns.append({'pattern': street_pat})

    # Component combinations
    escaped_city = re.escape(city) if city else None
    escaped_state = re.escape(state) if state else None
    escaped_zip = re.escape(zipcode) if zipcode else None

    if city and state:
        # City, State
        patterns.append({'pattern': rf'{escaped_city},?\s+{escaped_state}'})

    if city and state and zipcode:
        # City, State Zip
        patterns.append({'pattern': rf'{escaped_city},?\s+{escaped_state}\s+{escaped_zip}'})

    if city:
        # Street, City
        patterns.append({'pattern': rf'{street_pat},?\s+{escaped_city}'})

    # Full combined address (all provided components)
    if city or state or zipcode:
        full_parts = [street_pat]
        if city:
            full_parts.append(escaped_city)
        if state:
            full_parts.append(escaped_state)
        if zipcode:
            full_parts.append(escaped_zip)
        full_pattern = ',?\\s+'.join(full_parts)
        patterns.append({'pattern': full_pattern})

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
    Output: Literal strings and regex patterns covering individual names,
            combined forms, initials, titles, and middle-initial patterns.
    """
    variants = []

    first = first_name.strip()
    last = last_name.strip()
    first_initial = first[0] if first else ''

    # Individual components
    variants.append(first)  # John
    variants.append(last)   # Smith

    # Full name variants
    variants.append(f"{first} {last}")            # John Smith
    variants.append(f"{last}, {first}")            # Smith, John
    variants.append(f"{first_initial}. {last}")    # J. Smith
    variants.append(f"{last}, {first_initial}.")   # Smith, J.
    variants.append(f"{first_initial} {last}")     # J Smith

    # Case-insensitive full name
    name_pattern = rf'(?i){re.escape(first)}\s+{re.escape(last)}'
    variants.append({'pattern': name_pattern})

    # Last, First (case-insensitive)
    reverse_pattern = rf'(?i){re.escape(last)},?\s+{re.escape(first)}'
    variants.append({'pattern': reverse_pattern})

    # With middle initial: John A. Smith, John A Smith
    middle_init_pattern = rf'(?i){re.escape(first)}\s+[A-Z]\.?\s+{re.escape(last)}'
    variants.append({'pattern': middle_init_pattern})

    # Title patterns: Mr. Smith, Ms. Smith, Mrs. Smith, Dr. Smith
    title_pattern = rf'(?i)(?:Mr|Ms|Mrs|Dr|Prof)\.?\s+{re.escape(last)}'
    variants.append({'pattern': title_pattern})

    return variants


def generate_email_patterns(user: str, domain: str) -> list:
    """
    Generate patterns for an email address from user and domain components.

    Input: "john.smith", "acme.com"
    Output: Literals and patterns for the full email, individual components,
            and common obfuscated forms.
    """
    patterns = []

    user = user.strip().lower()
    domain = domain.strip().lower()
    full = f"{user}@{domain}"

    # Individual components
    patterns.append(user)
    patterns.append(domain)
    patterns.append(full)

    # Case-insensitive full email
    patterns.append({'pattern': rf'(?i){re.escape(user)}@{re.escape(domain)}'})

    # Obfuscated @ sign: [at], (at), {at}, " at "
    patterns.append({'pattern': rf'(?i){re.escape(user)}\s*[\[(\{{]?\s*at\s*[\])}}]?\s*{re.escape(domain)}'})

    # Obfuscated dots in domain: acme [dot] com, acme (dot) com
    domain_parts = domain.split('.')
    if len(domain_parts) >= 2:
        dot_pattern = r'\s*[\[(\{]?\s*dot\s*[\])\}]?\s*'.join(re.escape(p) for p in domain_parts)
        patterns.append({'pattern': rf'(?i){re.escape(user)}\s*[\[(\{{]?\s*at\s*[\])}}]?\s*{dot_pattern}'})

    # Partially masked: j***@acme.com, john.s****@acme.com
    if len(user) > 1:
        masked_user_pattern = rf'(?i){re.escape(user[0])}[*.\w]*@{re.escape(domain)}'
        patterns.append({'pattern': masked_user_pattern})

    # mailto: links
    patterns.append({'pattern': rf'(?i)mailto:\s*{re.escape(full)}'})

    return patterns


def generate_dob_patterns(month: int, day: int, year: int) -> list:
    """
    Generate patterns for a date of birth in all common formats.

    Input: month=3, day=15, year=1990
    Output: Literals and patterns for MM/DD/YYYY, Month DD YYYY,
            DD Mon YYYY, ISO format, and partial date combinations.
    """
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    month_abbrevs = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    patterns = []
    mm = f"{month:02d}"
    dd = f"{day:02d}"
    yyyy = str(year)
    yy = yyyy[-2:]
    name = month_names[month - 1]
    abbrev = month_abbrevs[month - 1]

    # US numeric formats: MM/DD/YYYY, MM-DD-YYYY, MM.DD.YYYY
    patterns.append({'pattern': rf'{mm}[-/\.]{dd}[-/\.]{yyyy}'})
    # With single-digit month/day: M/D/YYYY
    patterns.append({'pattern': rf'{month}[-/\.]{day}[-/\.]{yyyy}'})
    # Short year: MM/DD/YY
    patterns.append({'pattern': rf'{mm}[-/\.]{dd}[-/\.]{yy}'})

    dotstar_sep = r'[-/\.]'

    # ISO format: YYYY-MM-DD
    patterns.append(f"{yyyy}-{mm}-{dd}")

    # Written forms: March 15, 1990 / Mar    15, 1990
    name_pattern = rf'(?i)(?:{re.escape(name)}|{re.escape(abbrev)}\.?)\s+{day},?\s+{yyyy}'
    patterns.append({'pattern': name_pattern})

    # European written: 15 March 1990, 15 Mar 1990
    euro_pattern = rf'(?i){day}\s+(?:{re.escape(name)}|{re.escape(abbrev)}\.?)\s+{yyyy}'
    patterns.append({'pattern': euro_pattern})

    # Partial: Month Day (no year) — March 15, Mar 15
    partial_pattern = rf'(?i)(?:{re.escape(name)}|{re.escape(abbrev)}\.?)\s+{day}'
    patterns.append({'pattern': partial_pattern})

    # Partial: MM/DD (no year)
    patterns.append({'pattern': rf'{mm}[-/\.]{dd}'})

    # Month + year: March 1990, Mar 1990
    month_year_pattern = rf'(?i)(?:{re.escape(name)}|{re.escape(abbrev)}\.?)\s+{yyyy}'
    patterns.append({'pattern': month_year_pattern})

    return patterns


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

    try:
        patterns = generate_ssn_patterns(args.last4)
        add_to_section(config, 'ssn', patterns)
        print(f"Added SSN patterns for last 4: ***-**-{args.last4}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_address(args):
    """Handle address command."""
    config = load_yaml(args.config)

    patterns = generate_address_patterns(
        args.street,
        city=args.city,
        state=args.state,
        zipcode=args.zip
    )
    add_to_section(config, 'addresses', patterns)

    parts = [args.street]
    if args.city:
        parts.append(args.city)
    if args.state:
        parts.append(args.state)
    if args.zip:
        parts.append(args.zip)
    print(f"Added address patterns for: {', '.join(parts)}")

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

    variants = generate_name_variants(args.first, args.last)
    add_to_section(config, 'names', variants)
    print(f"Added name variants for: {args.first} {args.last}")

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_email(args):
    """Handle email command."""
    config = load_yaml(args.config)

    patterns = generate_email_patterns(args.user, args.domain)
    add_to_section(config, 'emails', patterns)
    print(f"Added email patterns for: {args.user}@{args.domain}")

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def cmd_dob(args):
    """Handle date of birth command."""
    config = load_yaml(args.config)

    patterns = generate_dob_patterns(args.month, args.day, args.year)
    add_to_section(config, 'dob', patterns)
    print(f"Added DOB patterns for: {args.month:02d}/{args.day:02d}/{args.year}")

    save_yaml(config, args.config)
    print(f"Updated: {args.config}")
    return 0


def _find_line_number(lines: list[str], value: str) -> int | None:
    """Find the 1-based line number of a value in the YAML file."""
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Match literal: "- CA" or "- 'CA'" or '- "CA"'
        if stripped == f"- {value}" or stripped == f"- '{value}'" or stripped == f'- "{value}"':
            return i + 1
        # Match pattern dict: "- pattern: '...'"
        if value.startswith("pattern: ") and value[9:] in stripped:
            return i + 1
    return None


def lint_config(config: dict, lines: list[str]) -> list[dict]:
    """
    Lint a PII config for common problems.

    Returns a list of warnings, each with 'section', 'value', 'line', 'rule', 'message'.
    """
    warnings = []

    for section, values in config.get('pii', {}).items():
        if not values or not isinstance(values, list):
            continue

        for v in values:
            if v is None:
                continue

            if isinstance(v, dict) and 'pattern' in v:
                # Regex pattern — check for missing word boundaries
                pattern = v['pattern']
                # Skip patterns that already have \b or use anchoring context
                # like \s, lookahead/behind, or start with non-word chars
                has_leading_boundary = pattern.startswith(r'\b') or pattern.startswith('(?')
                has_trailing_boundary = pattern.endswith(r'\b')

                # Extract the "core" text to estimate if it's a short token
                # Remove regex metacharacters to get approximate plain text
                core = re.sub(r'\\[bBdDwWsS]|\[\^?\]?[^\]]*\]|\{[^}]*\}|\([^)]*\)|[.+*?^$|\\]', '', pattern)
                core = core.strip()

                if len(core) <= 4 and core.isalpha() and not (has_leading_boundary and has_trailing_boundary):
                    fixed = pattern
                    if not has_leading_boundary:
                        fixed = r'\b' + fixed
                    if not has_trailing_boundary:
                        fixed = fixed + r'\b'
                    display = f"pattern: {pattern}"
                    warnings.append({
                        'section': section,
                        'value': display,
                        'line': _find_line_number(lines, display),
                        'rule': 'short-pattern-no-boundary',
                        'message': f"Short pattern may match inside longer words. Use:\n      pattern: '{fixed}'"
                    })
            else:
                # Literal string — short literals are prone to substring matches
                literal = str(v)
                if len(literal) <= 4 and literal.isalpha():
                    fixed_pattern = r'\b' + re.escape(literal) + r'\b'
                    warnings.append({
                        'section': section,
                        'value': literal,
                        'line': _find_line_number(lines, literal),
                        'rule': 'short-literal',
                        'message': f"Short literal \"{literal}\" may substring-match inside longer words. Replace with:\n      pattern: '{fixed_pattern}'"
                    })

    return warnings


def cmd_lint(args):
    """Lint a PII config for common problems."""
    config = load_yaml(args.config)

    with open(args.config, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    warnings = lint_config(config, lines)

    if not warnings:
        print(f"No issues found in {args.config}")
        return 0

    print(f"Found {len(warnings)} warning(s) in {args.config}:\n")
    for w in warnings:
        line_info = f"line {w['line']}" if w['line'] else "line ?"
        print(f"  [{w['section']}] {w['value']} ({line_info})")
        print(f"    {w['message']}")
        print()

    return 1


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
  %(prog)s ssn -c pii.yaml 6789
  %(prog)s cc -c pii.yaml 4111111111111234
  %(prog)s address -c pii.yaml --street "123 Main St" --city "Springfield" --state "IL" --zip "62701"
  %(prog)s name -c pii.yaml --first John --last Smith
  %(prog)s email -c pii.yaml --user john.smith --domain acme.com
  %(prog)s dob -c pii.yaml --month 3 --day 15 --year 1990
  %(prog)s lint -c pii.yaml
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
    ssn_parser.add_argument('last4', help='Last 4 digits of SSN')
    ssn_parser.set_defaults(func=cmd_ssn)

    # Address command
    addr_parser = subparsers.add_parser('address', help='Add address component patterns')
    addr_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    addr_parser.add_argument('--street', required=True, help='Street address (e.g., "123 Main St")')
    addr_parser.add_argument('--city', help='City name')
    addr_parser.add_argument('--state', help='State name or abbreviation')
    addr_parser.add_argument('--zip', help='ZIP code')
    addr_parser.set_defaults(func=cmd_address)

    # Credit card command
    cc_parser = subparsers.add_parser('cc', help='Add credit card patterns (matches masked versions with same last 4)')
    cc_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    cc_parser.add_argument('cards', nargs='+', help='Credit card numbers to add')
    cc_parser.set_defaults(func=cmd_cc)

    # Name command
    name_parser = subparsers.add_parser('name', help='Add name variants')
    name_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    name_parser.add_argument('--first', required=True, help='First name')
    name_parser.add_argument('--last', required=True, help='Last name')
    name_parser.set_defaults(func=cmd_name)

    # Email command
    email_parser = subparsers.add_parser('email', help='Add email address patterns')
    email_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    email_parser.add_argument('--user', required=True, help='Email username (before @)')
    email_parser.add_argument('--domain', required=True, help='Email domain (after @)')
    email_parser.set_defaults(func=cmd_email)

    # Date of birth command
    dob_parser = subparsers.add_parser('dob', help='Add date of birth patterns')
    dob_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    dob_parser.add_argument('--month', type=int, required=True, help='Month (1-12)')
    dob_parser.add_argument('--day', type=int, required=True, help='Day (1-31)')
    dob_parser.add_argument('--year', type=int, required=True, help='Four-digit year')
    dob_parser.set_defaults(func=cmd_dob)

    # Lint command
    lint_parser = subparsers.add_parser('lint', help='Check config for common problems')
    lint_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    lint_parser.set_defaults(func=cmd_lint)

    # Show command
    show_parser = subparsers.add_parser('show', help='Show current config')
    show_parser.add_argument('-c', '--config', type=Path, required=True, help='YAML config file')
    show_parser.set_defaults(func=cmd_show)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == '__main__':
    main()
