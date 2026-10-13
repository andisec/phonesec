# 📱 PhoneSec - Phone Number OSINT Tool

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Termux-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen.svg" alt="Maintained">
</p>

<p align="center">
  <strong>Advanced Phone Number Intelligence & OSINT Analysis Tool</strong>
</p>

---

## 📖 Deskripsi

**PhoneSec** adalah tool OSINT yang powerful untuk melakukan analisis mendalam terhadap nomor telepon. Tool ini menggunakan library `phonenumbers` dari Google untuk memberikan informasi komprehensif tentang nomor telepon, termasuk validasi, lokasi, carrier, timezone, dan format internasional.

### ✨ Fitur Utama

- 🔍 **Validasi Nomor** - Cek validitas dan kemungkinan nomor telepon
- 🌍 **Geolocation** - Identifikasi lokasi dan negara
- 📡 **Carrier Detection** - Deteksi provider/operator
- ⏰ **Timezone Info** - Informasi zona waktu
- 📞 **Format Conversion** - International, National, E164 format
- 📊 **Multiple Reports** - Output dalam JSON, HTML, dan TXT
- 📝 **Batch Processing** - Analisis multiple nomor sekaligus
- 🎨 **Colored Output** - Terminal output yang mudah dibaca
- 🔢 **Number Type Detection** - Mobile, Fixed Line, VoIP, dll

---

## 🚀 Instalasi

### 📱 Termux (Android)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install git python -y

# Clone repository
git clone https://github.com/andisec/phonesec.git

# Masuk ke direktori
cd phonesec

# Install Python dependencies
pip install -r requirements.txt

# Jalankan tool
python phonesec.py -h
```

### 🐧 Linux (Ubuntu/Debian/Kali)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install git python3 python3-pip -y

# Clone repository
git clone https://github.com/andisec/phonesec.git

# Masuk ke direktori
cd phonesec

# Install Python dependencies
pip3 install -r requirements.txt

# Jalankan tool
python3 phonesec.py -h
```

### 🪟 Windows

```powershell
# Install Python dari python.org jika belum ada
# Install Git dari git-scm.com jika belum ada

# Clone repository
git clone https://github.com/andisec/phonesec.git

# Masuk ke direktori
cd phonesec

# Install dependencies
pip install -r requirements.txt

# Jalankan tool
python phonesec.py -h
```

---

## 📚 Cara Penggunaan

### Basic Usage

```bash
# Analyze nomor dengan format internasional (+ prefix)
python phonesec.py -p +62812345678

# Analyze nomor dengan country code
python phonesec.py -p 081234567890 -c ID
```

### Advanced Usage

```bash
# Save JSON only
python phonesec.py -p +1234567890 -o json

# Save HTML only
python phonesec.py -p +1234567890 -o html

# Save TXT only
python phonesec.py -p +1234567890 -o txt

# Save both JSON & HTML (default)
python phonesec.py -p +1234567890 -o both

# Tanpa generate report
python phonesec.py -p +1234567890 --no-report
```

### Batch Mode

```bash
# Buat file phones.txt
echo "+62812345678" > phones.txt
echo "+1234567890" >> phones.txt
echo "+442012345678" >> phones.txt

# Run batch analysis
python phonesec.py -f phones.txt

# Batch dengan country code
python phonesec.py -f phones.txt -c US -o both
```

---

## 📊 Command Options

```
Usage: phonesec.py [OPTIONS]

Options:
  -p, --phone PHONE        Phone number untuk dianalisis (dengan + prefix)
  -f, --file FILE          File berisi list phone numbers (satu per baris)
  -c, --country CODE       Country code (e.g., US, ID, UK) jika nomor tanpa +
  -o, --output FORMAT      Output format: json, html, txt, atau both (default: both)
  --no-report              Skip pembuatan report file
  -h, --help               Tampilkan help message
```

---

## 📸 Screenshot Output

### Terminal Output
```
======================================================================
PHONE NUMBER ANALYSIS RESULTS
======================================================================

📱 Validation:
   Valid: True
   Possible: True

📞 Format Information:
   International: +62 812-3456-789
   National:      0812 3456 789
   E164:          +62812345678

🔢 Number Details:
   Country Code:  +62
   National No:   812345678
   Number Type:   Mobile

🌍 Location & Carrier:
   Location:      Indonesia
   Region Code:   ID
   Carrier:       Telkomsel
   Timezones:     Asia/Jakarta
======================================================================
```

---

## 📂 Struktur Project

```
phonesec/
├── phonesec.py              # Main executable script
├── requirements.txt         # Python dependencies
├── README.md                # Dokumentasi
├── LICENSE                  # MIT License
│
├── core/
│   ├── phone_analyzer.py    # Phone number analysis engine
│   └── reporter.py          # Report generation module
│
├── modules/
│   └── batch_analyzer.py    # Batch processing module
│
└── reports/                 # Generated reports folder
    ├── 62812345678_20241014_123456.json
    ├── 62812345678_20241014_123456.html
    └── 62812345678_20241014_123456.txt
```

---

## 🎯 Informasi yang Diperoleh

- ✅ **Validasi** - Apakah nomor valid dan possible
- 🌍 **Lokasi** - Negara dan region
- 📡 **Carrier** - Provider/operator telecom
- 🕐 **Timezone** - Zona waktu lokasi
- 📱 **Tipe** - Mobile, Fixed Line, VoIP, Toll Free, dll
- 🔢 **Format** - International, National, E164
- 🆔 **Country Code** - Kode negara
- 🔢 **National Number** - Nomor nasional

---

## 🎯 Use Cases

- 🔒 **Security Research** - Investigasi nomor mencurigakan
- 🕵️ **OSINT Investigation** - Intelligence gathering
- 📞 **Call Center** - Validasi nomor customer
- 🎓 **Education** - Pembelajaran telekomunikasi
- 🔍 **Verification** - Verifikasi nomor telepon
- 🚨 **Fraud Detection** - Deteksi nomor palsu/spam
- 📊 **Data Analysis** - Analisis database nomor telepon

---

## ⚠️ Disclaimer

**PENTING - BACA SEBELUM MENGGUNAKAN:**

Tool ini dibuat untuk tujuan yang **LEGAL dan ETIS** seperti:
- ✅ Penelitian keamanan yang sah dan berizin
- ✅ Verifikasi nomor telepon legitimate
- ✅ Analisis data untuk tujuan business intelligence
- ✅ Pembelajaran dan riset akademis
- ✅ Fraud prevention dan detection

**DILARANG** untuk:
- ❌ Harassment atau intimidasi
- ❌ Stalking atau tracking tanpa izin
- ❌ Pelanggaran privasi
- ❌ Spam atau telemarketing ilegal
- ❌ Aktivitas cybercrime
- ❌ Social engineering attack

**Pengguna bertanggung jawab penuh** atas penggunaan tool ini. Developer tidak bertanggung jawab atas penyalahgunaan tool ini.

---

## 🔧 Dependencies

- **Python 3.7+**
- **phonenumbers** - Google's phone number parsing library
- **requests** - HTTP library
- **colorama** - Colored terminal output
- **tabulate** - Table formatting

---

## 🛠️ Troubleshooting

### Error: Invalid phone number format
```bash
# Pastikan gunakan + prefix untuk format internasional
python phonesec.py -p +62812345678

# Atau gunakan country code
python phonesec.py -p 081234567890 -c ID
```

### Error: Module not found
```bash
pip install -r requirements.txt
```

### Nomor tidak terdeteksi carrier
```
Hal ini normal untuk beberapa nomor karena database carrier
tidak selalu lengkap untuk semua region/operator.
```

---

## 🤝 Contributing

Kontribusi selalu welcome! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

### Ide Kontribusi:
- Integration dengan API external (Truecaller, etc)
- Spam/scam detection database
- Machine learning untuk fraud detection
- GUI interface
- Export to CSV/Excel
- API server mode

---

## 📝 Changelog

### Version 1.0.0 (2024-10-14)
- ✨ Initial release
- 📱 Phone number validation & parsing
- 🌍 Geolocation detection
- 📡 Carrier identification
- ⏰ Timezone information
- 📊 Multiple report formats (JSON, HTML, TXT)
- 📝 Batch processing support
- 🎨 Colored terminal output

---

## 📄 License

MIT License

Copyright (c) 2024 AndiSec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 👨‍💻 Author

**AndiSec**
- GitHub: [@andisec](https://github.com/andisec)
- OSINTSEC: [osintsec](https://github.com/andisec/osintsec)
- PhoneSec: [phonesec](https://github.com/andisec/phonesec)

---

## ⭐ Support

Jika tool ini bermanfaat untuk Anda:
- ⭐ Berikan star di GitHub
- 🐛 Report bugs via Issues
- 💡 Suggest features via Issues
- 🔄 Share ke komunitas

---

## 📞 Contact & Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/andisec/phonesec/issues)
- 💡 **Feature Requests**: [GitHub Issues](https://github.com/andisec/phonesec/issues)
- 📧 **Email**: [Create an issue for contact]

---

<p align="center">
  <strong>Made with ❤️ for Security Researchers & OSINT Enthusiasts</strong>
</p>

<p align="center">
  <sub>Gunakan dengan bijak dan bertanggung jawab</sub>
</p>

---

## 🔗 Related Projects

- [OSINTSEC](https://github.com/andisec/osintsec) - Username OSINT Tool
- [Sherlock](https://github.com/sherlock-project/sherlock) - Username search
- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) - Phone OSINT framework

---

**⚡ Happy Hunting! ⚡**
