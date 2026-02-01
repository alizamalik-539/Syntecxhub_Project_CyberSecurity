import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b'sixteen_byte_key_for_aes_testing'

def encrypt(plaintext, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

print("--- Secure Chat Initialized ---")
print("Type your message and press Enter. Type 'exit' to quit.")

try:
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
            
        encrypted_data = encrypt(message, KEY)
        client.send(encrypted_data)
finally:
    client.close()
    print("Connection closed.")