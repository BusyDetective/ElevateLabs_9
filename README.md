# 🔐 Web Application Security Testing Lab (Flask-Based)

A full-stack **Web Application Security Testing Lab** built with Flask that combines:

- 🧪 Intentionally vulnerable web application endpoints  
- 🔍 Automated vulnerability scanner  
- 📊 Severity classification & PDF report generation  

This project simulates a real-world VAPT (Vulnerability Assessment & Penetration Testing) workflow by integrating both exploitation scenarios and automated detection logic into a single platform.

---

## 🚀 Project Overview

This lab environment includes:

### 🛠 Vulnerable Application Modules
- `/login` – Authentication bypass simulation (SQL Injection)
- `/search` – Query-based SQL injection testing
- `/feedback` – Reflected Cross-Site Scripting (XSS) simulation
- Forms intentionally lacking CSRF protection for detection testing

### 🔎 Integrated Vulnerability Scanner
- Automated form crawling
- Payload injection engine
- Response analysis & vulnerability detection
- Severity classification (Critical / High / Medium / Low)
- Automated PDF vulnerability report export

This allows testing both:
- Manual exploitation techniques  
- Automated vulnerability scanning logic  

---

## 🧠 Architecture & Workflow

1. User launches vulnerable web app
2. Scanner module crawls target endpoints
3. Forms & parameters are extracted
4. SQLi / XSS payloads are injected
5. HTTP responses are analyzed for exploit indicators
6. Vulnerabilities are classified
7. Structured PDF report is generated

Core scanning logic:
scanner/scanner_core.py

Main Flask application:
app.py

---

## 📊 Vulnerabilities Demonstrated

| Vulnerability | Implementation | Detection Method |
|--------------|---------------|------------------|
| SQL Injection | Authentication & search-based injection | Payload injection + response indicator analysis |
| XSS | Reflected script execution in feedback form | Script payload reflection detection |
| CSRF | Missing CSRF token protection | Token presence inspection |

---

## 🛠 Tech Stack

**Backend:** Python, Flask  
**Scanning Engine:** Custom modular scanner  
**Parsing:** BeautifulSoup  
**Reporting:** fpdf (PDF generation)  
**Database:** SQLite  
**Environment:** Kali Linux / Localhost  

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
