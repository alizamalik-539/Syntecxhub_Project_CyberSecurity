from cryptography.fernet import Fernet
import os
import sys

# --- CONFIGURATION ---
MASTER_PASSWORD = "admin"  # Change this to your desired master password
LOG_FILE = "passwords.txt"
KEY_FILE = "secret.key"

# --- 1. INITIALIZATION & KEY LOADING ---
def load_key():
    if not os.path.exists(KEY_FILE):
        print(f"❌ Error: {KEY_FILE} not found! Run your keygen.py first.")
        sys.exit()
    return open(KEY_FILE, "rb").read()

try:
    key = load_key()
    fernet = Fernet(key)
except Exception as e:
    print(f"❌ Encryption Error: {e}")
    sys.exit()

# --- 2. MASTER PASSWORD CHECK ---
print("--- 🔐 SECURE VAULT LOGIN ---")
auth = input("Enter Master Password: ")
if auth != MASTER_PASSWORD:
    print("❌ Access Denied! Incorrect Password.")
    sys.exit()
print("✅ Access Granted. Welcome back!\n")

# --- 3. ENCRYPT & ADD FUNCTION ---
def add():
    name = input('Account/Service Name: ')
    pwd = input("Password to save: ")
    
    # Encrypt
    encrypted_pwd = fernet.encrypt(pwd.encode()).decode()

    with open(LOG_FILE, 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print(f"✅ Securely saved password for {name}!")

# --- 4. DECRYPT & VIEW ALL ---
def view():
    if not os.path.exists(LOG_FILE):
        print("ℹ️  The vault is currently empty.")
        return

    print("\n--- 🗝️ YOUR STORED CREDENTIALS ---")
    with open(LOG_FILE, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data: continue
            
            user, passw = data.split("|")
            decrypted_pwd = fernet.decrypt(passw.encode()).decode()
            print(f"🌐 Service: {user:15} | 🔑 Password: {decrypted_pwd}")
    print("----------------------------------\n")

# --- 5. SEARCH FUNCTION (Added for extra credit!) ---
def search():
    target = input("Enter the service name to search for: ").lower()
    found = False
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            for line in f.readlines():
                user, passw = line.rstrip().split("|")
                if target in user.lower():
                    decrypted_pwd = fernet.decrypt(passw.encode()).decode()
                    print(f"🔍 Found: {user} | Password: {decrypted_pwd}")
                    found = True
    if not found:
        print("❌ No matching service found.")

# --- 6. MAIN INTERACTIVE MENU ---
while True:
    print("Options: (add), (view), (search), (q)uit")
    mode = input("Select an option: ").lower().strip()
    
    if mode in ["q", "quit", "exit"]:
        print("👋 Vault locked. Goodbye!")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "search":
        search()
    else:
        print("⚠️  Invalid choice. Please try again.")