import socket
from encrypt_helper import encrypt_helper

HOST = '127.0.0.1'
PORT = 12345

KEY = b'mysecretaeskey12'

encryptor = encrypt_helper(KEY)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
message = encryptor.encrypt("test1")
sock.sendall(message)
reply = sock.recv(4096)
print('Decrypted Reply:', encryptor.decrypt(reply))
message = encryptor.encrypt("test2")
sock.sendall(message)
reply = sock.recv(4096)
print('Decrypted Reply:', encryptor.decrypt(reply))

sock.close()
