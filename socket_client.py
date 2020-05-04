import socket

HOST = '202.182.125.155'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello world')
    data = s.recv(1024)

print('received', repr(data))