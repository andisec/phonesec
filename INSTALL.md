# PhoneSec Installation Guide

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation Methods

### Method 1: Install from source (Recommended)

```bash
# Clone the repository
git clone https://github.com/AndiSec/phonesec.git
cd phonesec

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x phonesec.py

# Run PhoneSec
./phonesec.py -h
```

### Method 2: Install as Python package

```bash
# From the project directory
pip install -e .

# Now you can run phonesec from anywhere
phonesec -h
```

### Method 3: Manual installation

```bash
# Install required packages
pip install phonenumbers>=8.13.0
pip install requests>=2.31.0
pip install colorama>=0.4.6
pip install tabulate>=0.9.0
pip install pytz>=2024.1

# Run the tool
python phonesec.py -h
```

## Quick Start

### Analyze a single phone number

```bash
# With international format
./phonesec.py -p +628123456789

# With country code
./phonesec.py -p 08123456789 -c ID
```

### Batch analysis

```bash
# Create a file with phone numbers (one per line)
echo "+1234567890" > phones.txt
echo "+628123456789" >> phones.txt

# Analyze all numbers
./phonesec.py -f phones.txt
```

### Output formats

```bash
# JSON only
./phonesec.py -p +628123456789 -o json

# HTML only
./phonesec.py -p +628123456789 -o html

# Text only
./phonesec.py -p +628123456789 -o txt

# Both JSON and HTML (default)
./phonesec.py -p +628123456789 -o both
```

## Troubleshooting

### Permission denied error

```bash
chmod +x phonesec.py
```

### Module not found error

Make sure you're in the correct directory and all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Python version error

Check your Python version:

```bash
python --version
# or
python3 --version
```

PhoneSec requires Python 3.7 or higher.

## Updating

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

## Uninstalling

```bash
# If installed as package
pip uninstall phonesec

# Or simply delete the directory
rm -rf phonesec/
```

## Support

For issues and questions:
- GitHub Issues: https://github.com/AndiSec/phonesec/issues
- Email: support@phonesec.com

## License

PhoneSec is released under the MIT License. See LICENSE file for details.
