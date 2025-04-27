import socket


HOST = '127.0.0.1'  
PORT = 12345         

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall("test1".encode("utf-8"))
reply = sock.recv(128)
print(reply.decode("utf-8"))
sock.sendall("test2".encode("utf-8"))
reply = sock.recv(128)
print(reply.decode("utf-8"))

sock.close()