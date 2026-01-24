import socket
import threading
from datetime import datetime

# ==========================================
# INTERNSHIP PROJECT: SMART PORT SCANNER
# TARGETS: Windows 10, Windows 7, Android
# ==========================================

# Your specific lab IP addresses
TARGET_IPS = ["192.168.100.73", "192.168.100.83", "192.168.100.69"]

# Common ports to scan (Web, Windows Sharing, Android Services)
PORT_RANGE = [21, 22, 23, 80, 135, 139, 443, 445, 3389, 8080, 5555]

LOG_FILE = "scan_report.txt"
print_lock = threading.Lock()

def scan_port(ip, port):
    """Attempts to connect to a specific IP and port."""
    try:
        # Create a socket object using TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)  # Wait 1.5 seconds for a response
        
        # connect_ex returns 0 if the connection is successful
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            with print_lock:
                status = f"[+] FOUND: {ip} has Port {port} OPEN"
                print(status)
                # Save the finding to the report file
                with open(LOG_FILE, "a") as f:
                    f.write(status + "\n")
        
        sock.close()
    except Exception:
        pass

def main():
    # 1. Initialize the Report File
    with open(LOG_FILE, "w") as f:
        f.write(f"CYBERSECURITY SCAN REPORT\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write("="*40 + "\n\n")

    print("\n" + "="*40)
    print("      🔍 STARTING MULTI-HOST SCAN 🔍      ")
    print("="*40)
    print(f"Scanning Targets: {TARGET_IPS}\n")

    threads = []

    # 2. Launch Threads for Speed
    for ip in TARGET_IPS:
        print(f"--- Processing IP: {ip} ---")
        for port in PORT_RANGE:
            # Create a thread for every single port to make it super fast
            t = threading.Thread(target=scan_port, args=(ip, port))
            threads.append(t)
            t.start()

    # 3. Join Threads (Wait for them to finish)
    for t in threads:
        t.join()

    print("\n" + "="*40)
    print(f"✅ SUCCESS: Results saved to {LOG_FILE}")
    print("="*40)

if __name__ == "__main__":
    main()