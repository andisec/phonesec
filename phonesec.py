#!/usr/bin/env python
"""
PhoneSec - Phone Number OSINT Tool
Author: AndiSec
Description: Comprehensive phone number analysis and OSINT tool
"""

import argparse
import sys
from pathlib import Path
from colorama import Fore, Style, init

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from core.phone_analyzer import PhoneAnalyzer
from core.reporter import Reporter
from modules.batch_analyzer import BatchAnalyzer

init(autoreset=True)

def print_banner():
    banner = f"""{Fore.CYAN}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║    ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗███████╗ ║
    ║    ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██╔════╝ ║
    ║    ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ███████╗ ║
    ║    ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║ ║
    ║    ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗███████║ ║
    ║    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ║
    ║                                                          ║
    ║              Phone Number OSINT Tool                     ║
    ║          Advanced Phone Intelligence Analysis            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    {Style.RESET_ALL}"""
    print(banner)

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description='PhoneSec - Phone Number OSINT Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -p +1234567890                     # Analyze single phone number
  %(prog)s -p 081234567890 -c ID              # Analyze with country code
  %(prog)s -p +1234567890 -o json             # Save as JSON only
  %(prog)s -p +1234567890 -o html             # Save as HTML only
  %(prog)s -p +1234567890 -o txt              # Save as TXT only
  %(prog)s -f phones.txt                      # Batch analyze from file
  %(prog)s -f phones.txt -c US -o both        # Batch with country code
        """
    )

    parser.add_argument('-p', '--phone', help='Phone number to analyze (with + prefix)')
    parser.add_argument('-f', '--file', help='File containing list of phone numbers (one per line)')
    parser.add_argument('-c', '--country', help='Country code (e.g., US, ID, UK) if number has no + prefix')
    parser.add_argument('-o', '--output', choices=['json', 'html', 'txt', 'both'], default='both',
                        help='Output format (default: both = json + html)')
    parser.add_argument('--no-report', action='store_true',
                        help='Skip generating report files')

    args = parser.parse_args()

    # Validate input
    if not args.phone and not args.file:
        parser.print_help()
        print(f"\n{Fore.RED}[!] Error: Please provide -p PHONE_NUMBER or -f FILE{Style.RESET_ALL}")
        sys.exit(1)

    # Initialize components
    analyzer = PhoneAnalyzer()
    reporter = Reporter()

    try:
        if args.file:
            # Batch mode
            batch = BatchAnalyzer(analyzer, reporter)
            batch.analyze_from_file(args.file, args.country, args.output)
        else:
            # Single phone number mode
            results = analyzer.analyze(args.phone, args.country)

            if results:
                # Print results
                analyzer.print_results()

                # Save reports
                if not args.no_report:
                    if args.output in ['json', 'both']:
                        reporter.save_json(args.phone, results)
                    if args.output in ['html', 'both']:
                        reporter.save_html(args.phone, results)
                    if args.output == 'txt':
                        reporter.save_txt(args.phone, results)

                print(f"{Fore.GREEN}[+] Analysis completed successfully!{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}[!] Failed to analyze phone number{Style.RESET_ALL}")
                sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
