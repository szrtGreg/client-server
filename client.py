# echo-client.py

import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

print('To login use pattern username:password')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(input('===> ').encode())
        data = s.recv(1024).decode()
        print(f'{data}')
