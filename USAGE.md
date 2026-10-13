# PhoneSec Usage Guide

## Quick Start

### Basic Usage

```bash
# Analyze a phone number with international format
./phonesec.py -p +628123456789

# Analyze without international prefix (requires country code)
./phonesec.py -p 08123456789 -c ID
```

## Command Line Options

### Required Arguments (one of these)

- `-p, --phone PHONE` - Single phone number to analyze
- `-f, --file FILE` - File containing multiple phone numbers (one per line)

### Optional Arguments

- `-c, --country COUNTRY` - Country code (e.g., US, ID, UK, AU, JP)
  - Required only if phone number doesn't have `+` prefix
  - Uses ISO 3166-1 alpha-2 country codes

- `-o, --output {json,html,txt,both}` - Output format
  - `json` - Save results as JSON only
  - `html` - Save results as HTML only  
  - `txt` - Save results as plain text only
  - `both` - Save as both JSON and HTML (default)

- `--no-report` - Skip generating report files
  - Results still shown in terminal
  - No files saved to reports directory

## Examples

### Single Number Analysis

```bash
# US number
./phonesec.py -p +14155552671

# Indonesian number
./phonesec.py -p +628123456789

# UK number
./phonesec.py -p +442071234567

# Without + prefix (must specify country)
./phonesec.py -p 08123456789 -c ID
./phonesec.py -p 4155552671 -c US
```

### Batch Processing

```bash
# Create a file with phone numbers
cat > phones.txt << EOF
+628123456789
+14155552671
+442071234567
+61212345678
EOF

# Analyze all numbers
./phonesec.py -f phones.txt

# With country code for numbers without +
./phonesec.py -f phones.txt -c ID

# Save as JSON only
./phonesec.py -f phones.txt -o json
```

### Output Formats

```bash
# JSON only (for automation/parsing)
./phonesec.py -p +628123456789 -o json

# HTML only (for viewing in browser)
./phonesec.py -p +628123456789 -o html

# Plain text only
./phonesec.py -p +628123456789 -o txt

# Both JSON and HTML (default)
./phonesec.py -p +628123456789 -o both

# No files, terminal output only
./phonesec.py -p +628123456789 --no-report
```

## Understanding the Output

### Terminal Output

PhoneSec displays comprehensive information in the terminal:

1. **Validation Status**
   - Valid: Whether the number is valid
   - Possible: Whether the number could exist

2. **Risk Assessment**
   - Risk level: LOW, MEDIUM, or HIGH
   - Risk score: 0-100
   - Risk factors detected

3. **Format Information**
   - International format: +XX XXX-XXX-XXXX
   - National format: (XXX) XXX-XXXX
   - E164 format: +XXXXXXXXXXXX

4. **Number Details**
   - Country code
   - National number
   - Number type (Mobile, Fixed Line, VoIP, etc.)

5. **Location & Carrier**
   - Geographic location
   - Region code
   - Carrier/operator name
   - Timezone(s)

6. **Current Time**
   - Local time in the number's timezone

7. **Map Links**
   - Google Maps link
   - OpenStreetMap link

8. **OSINT Links**
   - Google search
   - TrueCaller
   - WhatsApp
   - Telegram
   - Facebook
   - LinkedIn

### Report Files

Reports are saved in the `reports/` directory:

#### JSON Report
```json
{
  "phone_number": "+628123456789",
  "timestamp": "2024-01-01T12:00:00",
  "analysis": {
    "is_valid": true,
    "international_format": "+62 812-3456-789",
    "carrier": "Telkomsel",
    ...
  }
}
```

#### HTML Report
Beautiful, interactive HTML report with:
- Color-coded validation badges
- Organized sections
- Mobile-responsive design
- Easy to share

#### TXT Report
Plain text report suitable for:
- Command-line viewing
- Email
- Documentation

## Country Codes

Common country codes for `-c` option:

| Country | Code | Example Number |
|---------|------|----------------|
| United States | US | +1 415 555 2671 |
| Indonesia | ID | +62 812 3456 789 |
| United Kingdom | UK | +44 20 7123 4567 |
| Australia | AU | +61 2 1234 5678 |
| Japan | JP | +81 3 1234 5678 |
| Singapore | SG | +65 6123 4567 |
| Malaysia | MY | +60 12 345 6789 |
| Philippines | PH | +63 912 345 6789 |
| Thailand | TH | +66 81 234 5678 |
| Vietnam | VN | +84 91 234 5678 |

Full list: [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

## Tips and Best Practices

### Input Format

1. **Always use international format when possible**
   ```bash
   # Good
   ./phonesec.py -p +628123456789
   
   # Requires country code
   ./phonesec.py -p 08123456789 -c ID
   ```

2. **For batch processing, one number per line**
   ```
   +628123456789
   +14155552671
   +442071234567
   ```

3. **Remove spaces and dashes** (optional, but recommended)
   ```bash
   # Both work, but without formatting is cleaner
   ./phonesec.py -p +628123456789
   ./phonesec.py -p "+62 812-3456-789"
   ```

### Performance

- Batch processing is efficient for multiple numbers
- No API calls = fast analysis
- Results are instant (uses local phonenumbers library)

### Privacy

- All analysis is done locally
- No data sent to external servers
- OSINT links provided but not automatically accessed
- Safe to use with sensitive numbers

## Integration

### Use in Scripts

```bash
#!/bin/bash
# Analyze and save as JSON
./phonesec.py -p "$1" -o json --no-report > /tmp/result.txt
```

### Python API

```python
from core.phone_analyzer import PhoneAnalyzer
from core.reporter import Reporter

analyzer = PhoneAnalyzer()
reporter = Reporter()

# Analyze
results = analyzer.analyze("+628123456789")

# Print to terminal
analyzer.print_results()

# Save reports
reporter.save_json("+628123456789", results)
reporter.save_html("+628123456789", results)
```

## Troubleshooting

### Invalid Number Error

```
[!] Invalid phone number format
```

**Solutions:**
- Add `+` prefix or use `-c` option
- Check the number is complete
- Verify country code is correct

### Module Not Found

```
ModuleNotFoundError: No module named 'phonenumbers'
```

**Solution:**
```bash
pip install -r requirements.txt
```

### Permission Denied

```
bash: ./phonesec.py: Permission denied
```

**Solution:**
```bash
chmod +x phonesec.py
```

## Advanced Usage

### Automation

```bash
# Process all numbers in directory
for file in numbers/*.txt; do
    ./phonesec.py -f "$file" -o json
done

# Daily batch processing
0 0 * * * /path/to/phonesec.py -f /path/to/daily_numbers.txt
```

### Custom Output Directory

```python
from core.reporter import Reporter

reporter = Reporter(output_dir='custom_reports')
reporter.save_json(phone, results)
```

## Support

For questions and issues:
- GitHub: https://github.com/AndiSec/phonesec/issues
- Documentation: See README.md and INSTALL.md

## See Also

- [README.md](README.md) - Project overview
- [INSTALL.md](INSTALL.md) - Installation guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
