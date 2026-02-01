import socket
import threading # Required for "Multiple Clients"
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b'sixteen_byte_key_for_aes_testing'

def decrypt(combined_data, key):
    iv = combined_data[:16]
    ciphertext = combined_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} joined.")
    try:
        while True:
            data = conn.recv(1024)
            if not data: break
            
            decrypted = decrypt(data, KEY)
            print(f"[{addr}] Sent: {decrypted}")
            
            # --- REQUIREMENT: MESSAGE LOGGING ---
            with open("chat_log.txt", "a") as f:
                f.write(f"User {addr} sent encrypted: {data.hex()}\n")
    except:
        pass
    finally:
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()
print("Server is LISTENING for multiple clients...")

while True:
    conn, addr = server.accept()
    # This thread allows "Multiple Clients" to talk at once
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()