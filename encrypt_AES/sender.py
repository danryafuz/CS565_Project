import socket
from encrypt_helper import encrypt_helper

HOST = '192.168.12.51'
PORT = 12345
KEY = b'mysecretaeskey12'

encryptor = encrypt_helper(KEY)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

with open('data.txt', 'r') as file:
    lines = file.readlines()

sock.sendall(encryptor.encrypt("test1"))
reply = sock.recv(128)
print("Decrypted reply:", encryptor.decrypt(reply))

sock.sendall(encryptor.encrypt("test1"))
reply = sock.recv(128)
print("Decrypted reply:", encryptor.decrypt(reply))

for i in range(0, len(lines), 4):
    chunk = ''.join(lines[i:i+4])
    if chunk.strip():
        encrypted = encryptor.encrypt(chunk)
        sock.sendall(encrypted)

        reply = sock.recv(4096)
        print('Decrypted Reply:', encryptor.decrypt(reply))

sock.close()
