from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# AES_GCM Encryptor
class encrypt_helper:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        aesgcm = AESGCM(self.key)
        crypto_number = os.urandom(12) # Rnadom IV to more security and different data in packets
        cipher_text = aesgcm.encrypt(crypto_number, message.encode('utf-8'), None)
        return crypto_number + cipher_text

    def decrypt(self, encrypted_text):
        aesgcm = AESGCM(self.key)
        crypto_number = encrypted_text[:12]
        cipher_text = encrypted_text[12:]
        message = aesgcm.decrypt(crypto_number, cipher_text, None)
        return message.decode('utf-8')
