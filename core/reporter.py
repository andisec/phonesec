import json
from datetime import datetime
from pathlib import Path
from colorama import Fore, Style
from tabulate import tabulate

class Reporter:
    def __init__(self, output_dir='reports'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def save_json(self, phone_number, results):
        """Save results to JSON file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_number = phone_number.replace('+', '').replace(' ', '_')
        filename = self.output_dir / f"{safe_number}_{timestamp}.json"

        data = {
            'phone_number': phone_number,
            'timestamp': datetime.now().isoformat(),
            'analysis': results
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"{Fore.GREEN}[+] JSON report saved: {filename}{Style.RESET_ALL}")
        return filename

    def save_html(self, phone_number, results):
        """Save results to HTML file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_number = phone_number.replace('+', '').replace(' ', '_')
        filename = self.output_dir / f"{safe_number}_{timestamp}.html"

        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PhoneSec Report - {phone_number}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header .phone {{
            font-size: 1.5em;
            font-weight: 300;
            letter-spacing: 2px;
        }}
        .content {{
            padding: 40px;
        }}
        .status {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }}
        .status-badge {{
            padding: 15px 30px;
            border-radius: 25px;
            font-weight: bold;
            font-size: 1.1em;
        }}
        .valid {{
            background: #d4edda;
            color: #155724;
            border: 2px solid #28a745;
        }}
        .invalid {{
            background: #f8d7da;
            color: #721c24;
            border: 2px solid #dc3545;
        }}
        .section {{
            margin-bottom: 35px;
        }}
        .section h2 {{
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            font-size: 1.5em;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }}
        .info-card {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }}
        .info-card .label {{
            font-size: 0.9em;
            color: #666;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .info-card .value {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            word-break: break-all;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        .emoji {{
            font-size: 1.5em;
            margin-right: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📱 PhoneSec OSINT Report</h1>
            <div class="phone">{phone_number}</div>
            <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.9;">
                Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </p>
        </div>

        <div class="content">
            <div class="status">
                <div class="status-badge {'valid' if results['is_valid'] else 'invalid'}">
                    {'✓ VALID NUMBER' if results['is_valid'] else '✗ INVALID NUMBER'}
                </div>
                <div class="status-badge {'valid' if results['is_possible'] else 'invalid'}">
                    {'✓ POSSIBLE' if results['is_possible'] else '✗ NOT POSSIBLE'}
                </div>
            </div>

            <div class="section">
                <h2><span class="emoji">📞</span>Format Information</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">International Format</div>
                        <div class="value">{results['international_format']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">National Format</div>
                        <div class="value">{results['national_format']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">E164 Format</div>
                        <div class="value">{results['e164_format']}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2><span class="emoji">🔢</span>Number Details</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">Country Code</div>
                        <div class="value">{results['country_code']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">National Number</div>
                        <div class="value">{results['national_number']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Number Type</div>
                        <div class="value">{results['number_type']}</div>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2><span class="emoji">🌍</span>Location & Carrier</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">Location</div>
                        <div class="value">{results['location']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Region Code</div>
                        <div class="value">{results['region_code']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Carrier</div>
                        <div class="value">{results['carrier']}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Timezone(s)</div>
                        <div class="value">{', '.join(results['timezones'])}</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            <strong>PhoneSec</strong> - Phone Number OSINT Tool<br>
            Made with ❤️ for Security Researchers
        </div>
    </div>
</body>
</html>
"""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"{Fore.GREEN}[+] HTML report saved: {filename}{Style.RESET_ALL}")
        return filename

    def save_txt(self, phone_number, results):
        """Save results to TXT file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_number = phone_number.replace('+', '').replace(' ', '_')
        filename = self.output_dir / f"{safe_number}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("PHONESEC - PHONE NUMBER ANALYSIS REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Phone Number: {phone_number}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("VALIDATION\n")
            f.write("-" * 70 + "\n")
            f.write(f"Valid:    {results['is_valid']}\n")
            f.write(f"Possible: {results['is_possible']}\n\n")

            f.write("FORMAT INFORMATION\n")
            f.write("-" * 70 + "\n")
            f.write(f"International: {results['international_format']}\n")
            f.write(f"National:      {results['national_format']}\n")
            f.write(f"E164:          {results['e164_format']}\n\n")

            f.write("NUMBER DETAILS\n")
            f.write("-" * 70 + "\n")
            f.write(f"Country Code:  {results['country_code']}\n")
            f.write(f"National No:   {results['national_number']}\n")
            f.write(f"Number Type:   {results['number_type']}\n\n")

            f.write("LOCATION & CARRIER\n")
            f.write("-" * 70 + "\n")
            f.write(f"Location:      {results['location']}\n")
            f.write(f"Region Code:   {results['region_code']}\n")
            f.write(f"Carrier:       {results['carrier']}\n")
            f.write(f"Timezones:     {', '.join(results['timezones'])}\n\n")

            f.write("="*70 + "\n")
            f.write("Report generated by PhoneSec\n")

        print(f"{Fore.GREEN}[+] TXT report saved: {filename}{Style.RESET_ALL}")
        return filename
