import socket
import re

# 1. Our "Intelligence" Database
vulnerability_db = {
    "2.4.41": {"cve": "CVE-2021-40438", "severity": "CRITICAL", "fix": "Update to Apache 2.4.51 or higher."},
    "2.4.29": {"cve": "CVE-2019-0211", "severity": "HIGH", "fix": "Update to Apache 2.4.39 or higher."},
}

def generate_report(software, version, cve, severity, fix):
    report_content = f"""
    === VULNERABILITY SCAN REPORT ===
    Software: {software}
    Version:  {version}
    Status:   VULNERABLE
    CVE ID:   {cve}
    Severity: {severity}
    Recommendation: {fix}
    =================================
    """
    # This creates a file named 'scan_report.txt'
    with open("scan_report.txt", "w") as f:
        f.write(report_content)
    print("\n[+] Success! Report generated: scan_report.txt")

# --- EXECUTION FLOW ---
print("--- FINAL PHASE: FULL SCAN & REPORTING ---")

# Step 1 & 2: (Simulated for this final test)
target_software = "Apache"
target_version = "2.4.41"

# Step 3: Check DB
if target_version in vulnerability_db:
    data = vulnerability_db[target_version]
    # Step 4: Generate the File
    generate_report(target_software, target_version, data['cve'], data['severity'], data['fix'])
    print(f"Findings: {data['cve']} found!")
else:
    print("No vulnerabilities found.")