from pathlib import Path
from colorama import Fore, Style

class BatchAnalyzer:
    def __init__(self, analyzer, reporter):
        self.analyzer = analyzer
        self.reporter = reporter

    def analyze_from_file(self, filename, country_code=None, output_format='both'):
        """Analyze multiple phone numbers from a file"""
        try:
            with open(filename, 'r') as f:
                phone_numbers = [line.strip() for line in f if line.strip()]

            print(f"{Fore.CYAN}[*] Loaded {len(phone_numbers)} phone numbers from {filename}{Style.RESET_ALL}\n")

            all_results = {}
            success_count = 0
            failed_count = 0

            for idx, phone_number in enumerate(phone_numbers, 1):
                print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[*] Processing {idx}/{len(phone_numbers)}: {phone_number}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")

                results = self.analyzer.analyze(phone_number, country_code)

                if results:
                    all_results[phone_number] = results
                    success_count += 1

                    # Print results
                    self.analyzer.print_results()

                    # Save reports
                    if output_format in ['json', 'both']:
                        self.reporter.save_json(phone_number, results)
                    if output_format in ['html', 'both']:
                        self.reporter.save_html(phone_number, results)
                    if output_format == 'txt':
                        self.reporter.save_txt(phone_number, results)
                else:
                    failed_count += 1
                    print(f"{Fore.RED}[!] Failed to analyze: {phone_number}{Style.RESET_ALL}\n")

            # Summary
            print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}BATCH PROCESSING SUMMARY{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Successfully analyzed: {success_count}/{len(phone_numbers)}{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Failed: {failed_count}/{len(phone_numbers)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

            return all_results

        except FileNotFoundError:
            print(f"{Fore.RED}[!] Error: File '{filename}' not found{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return None
