import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fpdf import FPDF
import datetime


XSS_PAYLOAD = "<script>alert('XSS')</script>"
SQLI_PAYLOAD = "' OR '1'='1"

def is_vulnerable_xss(response_text, payload):
    variations = [
        payload.lower(),
        payload.replace("<", "&lt;").replace(">", "&gt;").lower(),
        "alert('xss')",
        "&lt;script&gt;alert('xss')&lt;/script&gt;",
        "<script>alert(\"xss\")</script>",
        "alert(\"xss\")"
    ]
    lowered = response_text.lower()
    return any(v in lowered for v in variations)

def is_vulnerable_sqli(response_text):
    lowered = response_text.lower()
    indicators = [
        "you have an error in your sql syntax",
        "unclosed quotation mark",
        "warning: mysql",
        "quoted string not properly terminated",
        "sql injection detected",
        "mysql_fetch",
        "native client",
        "odbc",
        "dashboard",
        "welcome",
        "logged in",
        "sqli detected",
        "sqli_success"
    ]
    return any(indicator in lowered for indicator in indicators)

def get_all_forms(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[ERROR] Getting forms: {e}")
        return []

def get_form_details(form):
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for tag in form.find_all(["input", "textarea"]):
        name = tag.attrs.get("name")
        input_type = tag.attrs.get("type", "text") if tag.name == "input" else "textarea"
        if name:
            inputs.append({"type": input_type, "name": name})

    return {"action": action, "method": method, "inputs": inputs}

def submit_form(form_details, base_url, payload, target_field=None):
    target_url = urljoin(base_url, form_details["action"])
    data = {}
    for i in form_details["inputs"]:
        if i["name"] == target_field:
            data[i["name"]] = payload
        elif i["type"] == "password":
            data[i["name"]] = "pass123"
        else:
            data[i["name"]] = "test"
    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data, timeout=10)
        else:
            return requests.get(target_url, params=data, timeout=10)
    except Exception as e:
        print(f"[ERROR] Submitting form to {target_url}: {e}")
        return None

def assign_severity(vuln_type):
    if "SQL" in vuln_type:
        return "High"
    elif "XSS" in vuln_type:
        return "Medium"
    elif "CSRF" in vuln_type:
        return "Low"
    else:
        return "Low"

def scan_target(target):
    results = []
    print(f"[INFO] Scanning: {target}")
    forms = get_all_forms(target)
    print(f"[INFO] Found {len(forms)} forms")

    found_vulns = {"XSS": False, "SQLi": False, "CSRF": False}

    for form in forms:
        details = get_form_details(form)
        input_names = [i['name'] for i in details["inputs"]]

        for input_field in input_names:
            if not found_vulns["XSS"]:
                res_xss = submit_form(details, target, XSS_PAYLOAD, input_field)
                if res_xss and is_vulnerable_xss(res_xss.text, XSS_PAYLOAD):
                    print(f"[VULN] XSS found on {target} in parameter '{input_field}'")
                    results.append({
                        "url": target,
                        "parameter": input_field,
                        "payload": XSS_PAYLOAD,
                        "vuln_type": "Cross-Site Scripting (XSS)",
                        "severity": assign_severity("XSS")
                    })
                    found_vulns["XSS"] = True

            if not found_vulns["SQLi"]:
                res_sqli = submit_form(details, target, SQLI_PAYLOAD, input_field)
                if res_sqli and is_vulnerable_sqli(res_sqli.text):
                    print(f"[VULN] SQLi found on {target} in parameter '{input_field}'")
                    results.append({
                        "url": target,
                        "parameter": input_field,
                        "payload": SQLI_PAYLOAD,
                        "vuln_type": "SQL Injection",
                        "severity": assign_severity("SQL Injection")
                    })
                    found_vulns["SQLi"] = True

        if not found_vulns["CSRF"] and details["method"] == "post":
            if not any("csrf" in i["name"].lower() for i in details["inputs"] if i["name"]):
                print(f"[VULN] Potential CSRF on {target}")
                results.append({
                    "url": target,
                    "parameter": ", ".join(input_names),
                    "payload": "-",
                    "vuln_type": "Missing CSRF Token",
                    "severity": assign_severity("CSRF")
                })
                found_vulns["CSRF"] = True

        if all(found_vulns.values()):
            break

    return results

def export_findings_to_pdf(findings, filename=None):
    if filename is None:
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"scan_report_{timestamp}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_title("Scan Report")

    pdf.cell(200, 10, txt="Scan Report", ln=True, align="C")
    pdf.ln(10)

    for finding in findings:
        pdf.set_font("Arial", style='B', size=11)
        pdf.cell(200, 10, f"Type: {finding['type']}", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, f"URL: {finding['url']}")
        pdf.multi_cell(0, 10, f"Payload: {finding['payload']}")
        pdf.multi_cell(0, 10, f"Severity: {finding['severity']}")
        pdf.ln(5)

    filepath = f"./static/reports/{filename}"
    pdf.output(filepath)
    return filepath
