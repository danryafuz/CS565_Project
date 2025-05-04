from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# AES_CFB Encryptor
class encrypt_helper:
    def __init__(self, key):
        self.key = key
        self.backend = default_backend()

    def encrypt(self, message):
        crypto_number = b'\x9c\x3a\x12\x7f\x44\xa0\xef\x01\x88\x5d\xc3\x7a\x6b\x9e\x4f\x25' # Constant IV to find
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
