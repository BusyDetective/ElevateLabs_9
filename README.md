# 🔐 Web Application Vulnerability Scanner (Flask-Based)

A Python-based **Web Application Vulnerability Scanner** built with Flask that automates detection of common OWASP Top 10 vulnerabilities including SQL Injection (SQLi), Cross-Site Scripting (XSS), and CSRF misconfigurations.

This project simulates a real-world VAPT workflow including automated payload injection, response analysis, severity classification, and PDF report generation.

---

## 🚀 Key Features

- 🔎 Automated scanning of HTML forms and GET parameters
- 🧪 Payload-based SQL Injection detection using response analysis
- 💉 Reflected XSS detection via script injection testing
- 🛡️ Basic CSRF vulnerability detection through token inspection
- 📊 Severity classification (Critical / High / Medium / Low)
- 📄 Automated PDF vulnerability report export
- 🧩 Built-in intentionally vulnerable demo endpoints for testing

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Scanning Engine:** Custom scanner_core.py
- **Payload Handling:** Modular payload injection logic
- **Parsing:** BeautifulSoup
- **Reporting:** fpdf (PDF generation)
- **Database:** SQLite
- **Environment:** Kali Linux / Localhost testing

---

## 🧠 Scanner Architecture

The scanner follows this workflow:

1. Crawl target page
2. Extract forms and input fields
3. Inject vulnerability-specific payloads
4. Analyze HTTP responses
5. Detect indicators of exploitation
6. Classify severity
7. Generate structured PDF report

Core scanning logic is implemented in:
scanner/scanner_core.py
---
---

## 📊 Vulnerability Detection Methods

| Vulnerability | Detection Logic |
|--------------|-----------------|
| SQL Injection | Injection of SQL payloads + detection of authentication bypass or alert triggers |
| XSS | Script payload reflection in HTTP response body |
| CSRF | Detection of missing CSRF tokens in form submissions |

---

## 📁 Project Structure
<pre> ElevateLabs_9/ 
├── app.py
├── setup_db.py
├── database.db
├── scanner/
│ ├── init.py
│ ├── scanner_core.py
│ ├── payloads.py
│ └── static/
├── static/
│ └── images/
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── scanner.html
│ ├── feedback.html
│ ├── login.html
│ └── search.html
├── screenshots/
│ ├── homepage.png
│ ├── scannerpage.png
│ └── scanreport.png
├── Project_Report_SQLi_Scanner.pdf
├── requirements.txt
└── README.md </pre>

---

## 🚀 How to Run

### 1.Clone the repo:
- git clone https://github.com/BusyDetective/ElevateLabs_9.git
- cd ElevateLabs_9

### 2. Install dependencies:
pip install -r requirements.txt

### 3. Create and activate a virtual environment:
- python -m venv venv
- source venv/bin/activate      # or venv\Scripts\activate on Windows 

### 4. Set up the database:
python setup_db.py

### 5. Run the app:
python app.py

The app will start at http://127.0.0.1:5000/

### 🛡️ Scanner Capabilities
| Vulnerability | Detection Method                                  |
| ------------- | ------------------------------------------------- |
| SQLi          | Payloads + alert injection detection in responses |
| XSS           | JavaScript payloads + reflection in HTML          |
| CSRF          | Absence of CSRF tokens in form submission         |

### 📄 Sample Report
A sample vulnerability report is included as:
Project_Report_SQLi_Scanner.pdf

### 📸 Screenshots
Screenshots of the UI are included in the /screenshots and /static/images/ directories.

### 📌 Notes:
- This project is built for educational and demonstration purposes only.
- Do not use this scanner on real websites without permission.
- Designed for running locally with intentionally vulnerable pages for practice.

### 👤 Author
- Kaivan Shah
- Cybersecurity | Penetration Testing
- Email: kaivanshah1810@gmail.com 
- GitHub: https://github.com/BusyDetective
