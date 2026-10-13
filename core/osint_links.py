from urllib.parse import quote
from colorama import Fore, Style
import pytz
from datetime import datetime

class OSINTLinks:
    """Generate OSINT search links for phone numbers"""

    @staticmethod
    def get_google_search(phone_number):
        """Generate Google search URL"""
        query = quote(phone_number)
        return f"https://www.google.com/search?q={query}"

    @staticmethod
    def get_truecaller_search(phone_number):
        """Generate TrueCaller search URL"""
        clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        return f"https://www.truecaller.com/search/{clean_number}"

    @staticmethod
    def get_whatsapp_link(phone_number):
        """Generate WhatsApp direct link"""
        clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        return f"https://wa.me/{clean_number}"

    @staticmethod
    def get_telegram_search(phone_number):
        """Generate Telegram search URL"""
        clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        return f"https://t.me/{clean_number}"

    @staticmethod
    def get_viber_link(phone_number):
        """Generate Viber direct link"""
        clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        return f"viber://contact?number={clean_number}"

    @staticmethod
    def get_facebook_search(phone_number):
        """Generate Facebook search URL"""
        query = quote(phone_number)
        return f"https://www.facebook.com/search/top/?q={query}"

    @staticmethod
    def get_linkedin_search(phone_number):
        """Generate LinkedIn search URL"""
        query = quote(phone_number)
        return f"https://www.linkedin.com/search/results/all/?keywords={query}"

    @staticmethod
    def get_instagram_search(phone_number):
        """Generate Instagram search hint"""
        return f"Search on Instagram app with: {phone_number}"

    @staticmethod
    def get_all_links(phone_number):
        """Get all OSINT links"""
        return {
            'google': OSINTLinks.get_google_search(phone_number),
            'truecaller': OSINTLinks.get_truecaller_search(phone_number),
            'whatsapp': OSINTLinks.get_whatsapp_link(phone_number),
            'telegram': OSINTLinks.get_telegram_search(phone_number),
            'viber': OSINTLinks.get_viber_link(phone_number),
            'facebook': OSINTLinks.get_facebook_search(phone_number),
            'linkedin': OSINTLinks.get_linkedin_search(phone_number),
            'instagram': OSINTLinks.get_instagram_search(phone_number)
        }

    @staticmethod
    def print_links(phone_number):
        """Print all OSINT links"""
        links = OSINTLinks.get_all_links(phone_number)

        print(f"{Fore.YELLOW}🔗 OSINT Search Links:{Style.RESET_ALL}")
        print(f"   Google:     {Fore.CYAN}{links['google']}{Style.RESET_ALL}")
        print(f"   TrueCaller: {Fore.CYAN}{links['truecaller']}{Style.RESET_ALL}")
        print(f"   WhatsApp:   {Fore.CYAN}{links['whatsapp']}{Style.RESET_ALL}")
        print(f"   Telegram:   {Fore.CYAN}{links['telegram']}{Style.RESET_ALL}")
        print(f"   Facebook:   {Fore.CYAN}{links['facebook']}{Style.RESET_ALL}")
        print(f"   LinkedIn:   {Fore.CYAN}{links['linkedin']}{Style.RESET_ALL}\n")


class LocationMapper:
    """Generate location and map links"""

    @staticmethod
    def get_google_maps_link(location, region_code=None):
        """Generate Google Maps search link"""
        if location and location != 'Unknown':
            query = quote(f"{location}")
            if region_code and region_code != 'Unknown':
                query = quote(f"{location}, {region_code}")
            return f"https://www.google.com/maps/search/{query}"
        return None

    @staticmethod
    def get_openstreetmap_link(location, region_code=None):
        """Generate OpenStreetMap search link"""
        if location and location != 'Unknown':
            query = quote(f"{location}")
            if region_code:
                query = quote(f"{location}, {region_code}")
            return f"https://www.openstreetmap.org/search?query={query}"
        return None

    @staticmethod
    def print_map_links(location, region_code):
        """Print map links"""
        gmaps = LocationMapper.get_google_maps_link(location, region_code)
        osm = LocationMapper.get_openstreetmap_link(location, region_code)

        if gmaps:
            print(f"{Fore.YELLOW}🗺️  Map Links:{Style.RESET_ALL}")
            print(f"   Google Maps:      {Fore.CYAN}{gmaps}{Style.RESET_ALL}")
            print(f"   OpenStreetMap:    {Fore.CYAN}{osm}{Style.RESET_ALL}\n")


class TimeInfo:
    """Get current time information for phone number timezone"""

    @staticmethod
    def get_current_time(timezone_str):
        """Get current time for a timezone"""
        try:
            if timezone_str and timezone_str != 'Unknown':
                tz = pytz.timezone(timezone_str)
                current_time = datetime.now(tz)
                return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        except:
            pass
        return None

    @staticmethod
    def print_time_info(timezones):
        """Print current time for timezones"""
        if timezones and timezones[0] != 'Unknown':
            print(f"{Fore.YELLOW}🕐 Local Time Information:{Style.RESET_ALL}")
            for tz in timezones:
                current_time = TimeInfo.get_current_time(tz)
                if current_time:
                    print(f"   {tz}: {Fore.GREEN}{current_time}{Style.RESET_ALL}")
            print()


class RiskAssessment:
    """Basic risk assessment for phone numbers"""

    @staticmethod
    def assess_risk(results):
        """Assess basic risk score"""
        risk_score = 0
        risk_factors = []

        # Invalid number
        if not results.get('is_valid'):
            risk_score += 30
            risk_factors.append('Invalid number format')

        # Not possible
        if not results.get('is_possible'):
            risk_score += 20
            risk_factors.append('Number not possible')

        # Unknown carrier (could be VoIP or unregistered)
        if results.get('carrier') == 'Unknown':
            risk_score += 15
            risk_factors.append('Unknown carrier (possible VoIP)')

        # VoIP numbers
        if 'VoIP' in results.get('number_type', ''):
            risk_score += 25
            risk_factors.append('VoIP number (higher fraud risk)')

        # Toll Free / Premium
        number_type = results.get('number_type', '')
        if 'Premium' in number_type:
            risk_score += 20
            risk_factors.append('Premium rate number')
        elif 'Toll Free' in number_type:
            risk_score += 5
            risk_factors.append('Toll-free number')

        # Unknown location
        if results.get('location') == 'Unknown':
            risk_score += 10
            risk_factors.append('Unknown location')

        # Determine risk level
        if risk_score >= 50:
            risk_level = 'HIGH'
            color = Fore.RED
        elif risk_score >= 25:
            risk_level = 'MEDIUM'
            color = Fore.YELLOW
        else:
            risk_level = 'LOW'
            color = Fore.GREEN

        return {
            'score': risk_score,
            'level': risk_level,
            'color': color,
            'factors': risk_factors
        }

    @staticmethod
    def print_risk_assessment(results):
        """Print risk assessment"""
        risk = RiskAssessment.assess_risk(results)

        print(f"{Fore.YELLOW}⚠️  Risk Assessment:{Style.RESET_ALL}")
        print(f"   Risk Level: {risk['color']}{risk['level']} ({risk['score']}/100){Style.RESET_ALL}")

        if risk['factors']:
            print(f"   Risk Factors:")
            for factor in risk['factors']:
                print(f"     • {Fore.YELLOW}{factor}{Style.RESET_ALL}")
        else:
            print(f"   {Fore.GREEN}No significant risk factors detected{Style.RESET_ALL}")
        print()

        return risk
