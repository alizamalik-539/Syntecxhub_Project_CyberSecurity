from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# 1. Generate a random 32-byte key (Keep this secret!)
# In a real app, you'd share this via a Key Exchange.
key = b'sixteen_byte_key_for_aes_testing' # Exactly 32 bytes for AES-256

def encrypt(plaintext, key):
    # 2. Generate a random IV (16 bytes for AES)
    iv = os.urandom(16)
    
    # 3. Setup the Cipher
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 4. Encrypt the message
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    
    # 5. Return IV + Ciphertext (The receiver needs the IV to decrypt!)
    return iv + ciphertext

def decrypt(combined_data, key):
    # 1. Extract the IV (first 16 bytes) and the actual ciphertext
    iv = combined_data[:16]
    ciphertext = combined_data[16:]
    
    # 2. Setup the Cipher for decryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # 3. Decrypt and return
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()

# --- TESTING IT ---
msg = "Hello Server! This is secret."
encrypted_stuff = encrypt(msg, key)
print(f"Scrambled: {encrypted_stuff.hex()}")

decrypted_msg = decrypt(encrypted_stuff, key)
print(f"Back to normal: {decrypted_msg}")