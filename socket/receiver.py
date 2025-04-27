import socket

HOST = '127.0.0.1'  
PORT = 12345  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

print('Receiver up')

conn, addr = sock.accept()
while True:
    msg = conn.recv(1024)
    if not msg: continue
    conn.send("received".encode("utf-8"))
    print('Message:', msg.decode("utf-8"))

sock.close()