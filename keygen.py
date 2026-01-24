from cryptography.fernet import Fernet

def generate_key():
    # This generates a random secure key
    key = Fernet.generate_key()
    
    # We save this key to a file called 'secret.key'
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    
    print("✅ Success! 'secret.key' has been created.")
    print("⚠️  Warning: Keep this file safe. Without it, you cannot decrypt your passwords.")

if __name__ == "__main__":
    generate_key()