This project is a network security tool built using Python to identify open ports on a target host. It allows an auditor to scan a specific IP address or a range of devices to determine which services are active and potentially vulnerable.

By using the Three-Way Handshake (SYN, SYN-ACK, ACK) logic, the script attempts to establish a connection with the target. If the connection is successful, the port is flagged as OPEN.

🚀 Key Features
Multi-Target Capability: Scans multiple IP addresses (Windows 7, Windows 10, and Android) in a single run.

High Performance: Implemented Multi-threading using the threading library to scan dozens of ports simultaneously, significantly reducing scan time.

Protocol Support: Utilizes the socket library to communicate over the TCP protocol.

Logging: Automatically generates a scan_report.txt file containing the timestamp and the results of the scan for official documentation.

🛠️ Technical Implementation
Language: Python 3.x

Libraries: socket, threading, datetime

Concurrency: ThreadPoolExecutor / Threading logic for parallel processing.

📊 How to Use
Open scanner.py.

Update the targets list with your laboratory IP addresses.

Run the script: python scanner.py.

Review the results in the terminal or the generated scan_report.txt.
