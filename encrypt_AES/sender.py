import socket
from encrypt_helper import encrypt_helper

HOST = '127.0.0.1'
PORT = 12345
KEY = b'mysecretaeskey12'

encryptor = encrypt_helper(KEY)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(encryptor.encrypt("test1"))
reply = sock.recv(128)
print("Decrypted reply:", encryptor.decrypt(reply))

sock.sendall(encryptor.encrypt("test2"))
reply = sock.recv(128)
print("Decrypted reply:", encryptor.decrypt(reply))

sock.close()
