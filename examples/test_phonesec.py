#!/usr/bin/env python
"""Example usage of PhoneSec"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.phone_analyzer import PhoneAnalyzer
from core.reporter import Reporter
from core.osint_links import OSINTLinks, RiskAssessment

def test_single_number():
    """Test analyzing a single phone number"""
    print("Testing single phone number analysis...\n")

    analyzer = PhoneAnalyzer()
    reporter = Reporter(output_dir='../reports')

    # Example: Indonesian number
    phone = "+628123456789"

    results = analyzer.analyze(phone)

    if results:
        analyzer.print_results()

        # Generate risk assessment
        risk = RiskAssessment.assess_risk(results)
        print(f"Risk Level: {risk['level']} ({risk['score']}/100)")

        # Save reports
        reporter.save_json(phone, results)
        reporter.save_html(phone, results)

        print("\n✓ Test completed successfully!")
    else:
        print("✗ Test failed!")

def test_osint_links():
    """Test OSINT link generation"""
    print("\nTesting OSINT link generation...\n")

    phone = "+1234567890"
    links = OSINTLinks.get_all_links(phone)

    print("Generated OSINT Links:")
    for platform, url in links.items():
        print(f"  {platform:12} : {url}")

    print("\n✓ OSINT links generated successfully!")

def test_number_formats():
    """Test different number formats"""
    print("\nTesting different number formats...\n")

    analyzer = PhoneAnalyzer()

    test_numbers = [
        ("+628123456789", None, "Indonesian with +"),
        ("08123456789", "ID", "Indonesian without +"),
        ("+14155552671", None, "US with +"),
        ("4155552671", "US", "US without +"),
    ]

    for phone, country, description in test_numbers:
        print(f"Testing: {description}")
        print(f"Input: {phone}" + (f" (Country: {country})" if country else ""))

        parsed = analyzer.parse_number(phone, country)

        if parsed:
            print(f"✓ Parsed successfully: {parsed}")
        else:
            print("✗ Failed to parse")
        print()

if __name__ == '__main__':
    print("="*70)
    print("PhoneSec - Example Usage & Testing")
    print("="*70 + "\n")

    try:
        test_single_number()
        test_osint_links()
        test_number_formats()

        print("\n" + "="*70)
        print("All tests completed!")
        print("="*70)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
