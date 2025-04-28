import socket
from encrypt_helper import encrypt_helper

HOST = '127.0.0.1'
PORT = 12345
KEY = b'mysecretaeskey12'

encryptor = encrypt_helper(KEY)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

print('Receiver up and running.')

conn, addr = sock.accept()
print(f"Connected by {addr}")

while True:
    msg = conn.recv(4096)
    if not msg:
        print('no package received, disconnecting')
        break
    decrypted_msg = encryptor.decrypt(msg)
    print('Decrypted Message:', decrypted_msg)
    response = encryptor.encrypt("received")
    conn.sendall(response)

sock.close()
