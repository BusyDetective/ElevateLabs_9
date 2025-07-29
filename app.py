from flask import Flask, render_template, request, redirect, url_for, session, send_file
from scanner.scanner_core import scan_target
import sqlite3
import io
from datetime import datetime
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    sqli_success = False

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # Detect basic SQLi patterns
        combined = f"{username} {password}".lower()
        if any(p in combined for p in ["'", '"', "--", "or", "1=1", ";"]):
            sqli_success = True

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] SQL Query: {query}")

        try:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()  
            c.execute(query)
            user = c.fetchone()
            conn.close()

            if user:
                session["user"] = user[0]
                return render_template("login.html", sqli_success=sqli_success)
            else:
                error = "Invalid credentials"
        except Exception as e:
            error = f"SQL Error: {e}"

    return render_template("login.html", error=error, sqli_success=sqli_success)

@app.route("/search", methods=["GET", "POST"])
def search():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    sqli_success = False
    results = []
    query = ""

    if request.method == "POST":
        keyword = request.form["search"].strip()
        if keyword:
            query = f"SELECT * FROM products WHERE name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
            if any(payload in keyword.lower() for payload in ["'", '"', "--", "or", "1=1", ";"]):
                sqli_success = True
        else:
            query = "SELECT * FROM products"
    else:
        query = "SELECT * FROM products"

    try:
        print(f"[DEBUG] SQL Query: {query}")
        c.execute(query)
        results = c.fetchall()
    except Exception as e:
        print(f"[ERROR] SQL execution failed: {e}")
        results = []
        sqli_success = True
    finally:
        conn.close()

    return render_template("search.html", results=results, sqli_success=sqli_success)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    feedback_input = None
    if request.method == "POST":
        feedback_input = request.form.get("feedback")
    return render_template("feedback.html", feedback_input=feedback_input)

@app.route("/scanner", methods=["GET", "POST"])
def scanner():
    if request.method == "POST":
        target_url = request.form.get("target")  # ✅ Match 'target' from the form
        if not target_url:
            return "Target URL required", 400

        try:
            results = scan_target(target_url)
            session["findings"] = results
            return render_template("scanner.html", findings=results)
        except Exception as e:
            return f"Error scanning target: {str(e)}", 500

    # For GET requests
    return render_template("scanner.html")

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, "Vulnerability Scan Report", ln=True, align="C")
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.5)
        self.line(10, 22, 287, 22)  # horizontal divider
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 9)
        self.set_text_color(130, 130, 130)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


@app.route("/download_report")
def download_report():
    findings = session.get("findings", [])

    pdf = PDFReport(orientation='L')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)

    # Column headers
    headers = ["URL", "Parameter", "Payload", "Vulnerability", "Severity"]
    col_widths = [80, 35, 60, 50, 40]

    # Header Row
    pdf.set_fill_color(44, 62, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 11)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", "", 10)
    fill = False
    for f in findings:
        url = str(f.get("url", ""))
        param = str(f.get("parameter", ""))
        payload = str(f.get("payload", ""))
        vuln = str(f.get("vuln_type", ""))
        severity = str(f.get("severity", ""))

        # Severity color logic
        if severity.lower() == "high":
            pdf.set_text_color(192, 57, 43)  # red
        elif severity.lower() == "medium":
            pdf.set_text_color(243, 156, 18)  # orange
        elif severity.lower() == "low":
            pdf.set_text_color(39, 174, 96)  # green
        else:
            pdf.set_text_color(44, 62, 80)  # default gray

        # Alternating row fill
        if fill:
            pdf.set_fill_color(245, 245, 245)
        else:
            pdf.set_fill_color(255, 255, 255)

        row = [url, param, payload, vuln, severity]
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, item, border=1, align="L", fill=True)
        pdf.ln()
        fill = not fill  # toggle

    pdf_output = pdf.output(dest='S').encode('latin-1')
    return send_file(
        io.BytesIO(pdf_output),
        as_attachment=True,
        download_name="vulnerability_report.pdf",
        mimetype="application/pdf"
    )


@app.route("/export_pdf")
def export_pdf():
    findings = session.get("scan_results", [])
    if not findings:
        return "No scan results available to export", 400

    pdf_path = export_findings_to_pdf(findings)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
