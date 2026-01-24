# Syntecxhub Cybersecurity Internship - Projects

This repository contains the completed tasks for my Cybersecurity Internship at **Syntecxhub**. 

## 🛡️ Project 1: Multi-Target Port Scanner
A Python-based network reconnaissance tool designed to identify active services across multiple devices.

### Features:
- **Multi-Host Scanning:** Simultaneously scans Windows 7, Windows 10, and Android devices.
- **Concurrency:** Uses `threading` to perform high-speed scans.
- **Protocol:** Implements TCP Three-Way Handshake logic using the `socket` library.
- **Reporting:** Automatically logs open ports to `scan_report.txt`.

---

## 🔐 Project 2: AES Password Manager
A secure cryptographic vault for local credential storage.

### Features:
- **Encryption:** Uses **AES-128 Symmetric Encryption** via the `cryptography` library (Fernet).
- **Security Gate:** Implemented a **Master Password** authentication system.
- **Functionality:** Supports adding, retrieving, and searching for encrypted credentials.
- **Persistence:** Securely saves encrypted cipher-text to a local file, ensuring zero plain-text storage.

### How to Run:
1. Install dependencies: `pip install cryptography`
2. Run `keygen.py` once to generate your encryption key.
3. Run `manager.py` to access the vault.

Run the script: python scanner.py.

Review the results in the terminal or the generated scan_report.txt.
