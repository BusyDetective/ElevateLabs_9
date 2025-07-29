# 🔍 Web Application Vulnerability Scanner

A lightweight, modern Python-based web vulnerability scanner built with Flask. It scans target URLs for critical OWASP Top 10 vulnerabilities like SQL Injection, XSS, and Missing CSRF Tokens — with a PDF report export feature.

---

## 📌 Features

- ✅ Detects:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Missing CSRF Tokens
- ✅ PDF export of scan results
- ✅ Clean Bootstrap-based UI
- ✅ Modular codebase (scanner_core, payloads)

---

## 🛠 Tools & Tech Stack

- Python
- Flask
- BeautifulSoup
- Requests
- FPDF (for PDF generation)
- HTML/CSS (Jinja2 templates)

---

## 📷 Screenshots

| Home Page | Scanner Interface | PDF Report |
|-----------|-------------------|------------|
| ![](screenshots/homepage.png) | ![](screenshots/scannerpage.png) | ![](screenshots/reportpage.png) |

---

## 📝 How to Run

1. Clone the repo:
git clone https://github.com/BusyDetective/ElevateLabs_9.git

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows

3. Install dependencies:

4. Run the application:
python app.py

5. Visit http://localhost:5000 in your browser.

Directory Structure:
WebVulnScanner/
├── app.py
├── setup_db.py
├── database.db
├── scanner/
│   ├── __init__.py
│   ├── scanner_core.py
│   ├── payloads.py
│   └── static/
├── static/
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── scanner.html
│   ├── feedback.html
│   ├── login.html
│   └── search.html
├── scan_report.pdf
└── screenshots/
    ├── home.png
    ├── scanner.png
    └── report.png

👤 Author
Kaivan Shah
Cybersecurity | Penetration Testing
Email: kaivanshah1810@gmail.com
GitHub: BusyDetective

🚀 If you found this project useful, feel free to give it a ⭐ on GitHub!
