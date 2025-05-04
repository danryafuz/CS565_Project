import socket
from encrypt_helper import encrypt_helper

HOST = '192.168.12.51'
PORT = 12345
KEY = b'mysecretaeskey12'

encryptor = encrypt_helper(KEY)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

print('Receiver up')

conn, addr = sock.accept()
while True:
    msg = conn.recv(1024)
    if not msg: 
        print('no package received, disconnecting')
        break
    try:
        print(msg)
        plaintext = encryptor.decrypt(msg)
        print('Decrypted Message:', plaintext)
        conn.send(encryptor.encrypt("received"))
    except Exception as e:
        print("Error decrypting:", e)

sock.close()