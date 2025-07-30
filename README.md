# WebVulnScanner 🔍

A lightweight **Web Application Vulnerability Scanner** with a web-based interface built using **Flask**. This tool is designed to identify common OWASP vulnerabilities such as:

- ✅ SQL Injection (SQLi)
- ✅ Cross-Site Scripting (XSS)
- ✅ Cross-Site Request Forgery (CSRF)

---

## 🧩 Features

- 🔍 **Automated vulnerability scanning** of forms and GET parameters
- ⚠️ **SQLi detection** using payload analysis and response inspection
- ⚠️ **XSS detection** by injecting payloads and detecting reflected scripts
- ⚠️ **Basic CSRF detection** by analyzing missing tokens in forms
- 📄 **PDF export** of scan results
- 📷 **UI screenshots** and a detailed project report
- 🖼️ **Vulnerable demo pages** (`/login`, `/feedback`, `/search`) for testing

---

## 📁 Project Structure
<pre> 
ElevateLabs_9/ 
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
