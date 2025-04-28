from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class encrypt_helper:
    def __init__(self, key):
        self.key = key
        self.backend = default_backend()

    def encrypt(self, message):
        crypto_number = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(crypto_number), backend=self.backend)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(message.encode('utf-8')) + encryptor.finalize()
        return crypto_number + cipher_text

    def decrypt(self, encrypted_text):
        crypto_number = encrypted_text[:16]
        ciphertext = encrypted_text[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(crypto_number), backend=self.backend)
        decryptor = cipher.decryptor()
        message = decryptor.update(ciphertext) + decryptor.finalize()
        return message.decode('utf-8')
