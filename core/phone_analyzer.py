import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style
import json

class PhoneAnalyzer:
    def __init__(self):
        self.results = {}

    def parse_number(self, phone_number, country_code=None):
        """Parse and validate phone number"""
        try:
            if country_code:
                parsed = phonenumbers.parse(phone_number, country_code)
            else:
                # Try to parse with + prefix
                if not phone_number.startswith('+'):
                    phone_number = '+' + phone_number
                parsed = phonenumbers.parse(phone_number, None)

            return parsed
        except phonenumbers.NumberParseException as e:
            return None

    def analyze(self, phone_number, country_code=None):
        """Comprehensive phone number analysis"""
        print(f"\n{Fore.CYAN}[*] Analyzing phone number: {Fore.YELLOW}{phone_number}{Style.RESET_ALL}\n")

        # Parse number
        parsed = self.parse_number(phone_number, country_code)

        if not parsed:
            print(f"{Fore.RED}[!] Invalid phone number format{Style.RESET_ALL}")
            return None

        # Basic Info
        self.results = {
            'input': phone_number,
            'international_format': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            'national_format': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
            'e164_format': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
            'country_code': f'+{parsed.country_code}',
            'national_number': parsed.national_number,
        }

        # Validation
        self.results['is_valid'] = phonenumbers.is_valid_number(parsed)
        self.results['is_possible'] = phonenumbers.is_possible_number(parsed)

        # Number Type
        number_type = phonenumbers.number_type(parsed)
        type_mapping = {
            0: 'Fixed Line',
            1: 'Mobile',
            2: 'Fixed Line or Mobile',
            3: 'Toll Free',
            4: 'Premium Rate',
            5: 'Shared Cost',
            6: 'VoIP',
            7: 'Personal Number',
            8: 'Pager',
            9: 'UAN',
            10: 'Voicemail',
            99: 'Unknown'
        }
        self.results['number_type'] = type_mapping.get(number_type, 'Unknown')

        # Location
        location = geocoder.description_for_number(parsed, 'en')
        self.results['location'] = location if location else 'Unknown'

        # Carrier
        carrier_name = carrier.name_for_number(parsed, 'en')
        self.results['carrier'] = carrier_name if carrier_name else 'Unknown'

        # Timezone
        timezones = timezone.time_zones_for_number(parsed)
        self.results['timezones'] = list(timezones) if timezones else ['Unknown']

        # Region Code
        region = phonenumbers.region_code_for_number(parsed)
        self.results['region_code'] = region if region else 'Unknown'

        return self.results

    def print_results(self):
        """Print analysis results with colors"""
        if not self.results:
            print(f"{Fore.RED}[!] No analysis data available{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}PHONE NUMBER ANALYSIS RESULTS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

        # Validation Status
        valid_color = Fore.GREEN if self.results['is_valid'] else Fore.RED
        print(f"{Fore.YELLOW}📱 Validation:{Style.RESET_ALL}")
        print(f"   Valid: {valid_color}{self.results['is_valid']}{Style.RESET_ALL}")
        print(f"   Possible: {Fore.GREEN if self.results['is_possible'] else Fore.RED}{self.results['is_possible']}{Style.RESET_ALL}\n")

        # Format Information
        print(f"{Fore.YELLOW}📞 Format Information:{Style.RESET_ALL}")
        print(f"   International: {Fore.GREEN}{self.results['international_format']}{Style.RESET_ALL}")
        print(f"   National:      {Fore.GREEN}{self.results['national_format']}{Style.RESET_ALL}")
        print(f"   E164:          {Fore.GREEN}{self.results['e164_format']}{Style.RESET_ALL}\n")

        # Number Details
        print(f"{Fore.YELLOW}🔢 Number Details:{Style.RESET_ALL}")
        print(f"   Country Code:  {Fore.GREEN}{self.results['country_code']}{Style.RESET_ALL}")
        print(f"   National No:   {Fore.GREEN}{self.results['national_number']}{Style.RESET_ALL}")
        print(f"   Number Type:   {Fore.GREEN}{self.results['number_type']}{Style.RESET_ALL}\n")

        # Location & Carrier
        print(f"{Fore.YELLOW}🌍 Location & Carrier:{Style.RESET_ALL}")
        print(f"   Location:      {Fore.GREEN}{self.results['location']}{Style.RESET_ALL}")
        print(f"   Region Code:   {Fore.GREEN}{self.results['region_code']}{Style.RESET_ALL}")
        print(f"   Carrier:       {Fore.GREEN}{self.results['carrier']}{Style.RESET_ALL}")
        print(f"   Timezones:     {Fore.GREEN}{', '.join(self.results['timezones'])}{Style.RESET_ALL}\n")

        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

    def get_json(self):
        """Return results as JSON string"""
        return json.dumps(self.results, indent=2)
