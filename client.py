

import socket

HOST = '127.0.0.1'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = input("Enter your message here: ")
client.sendall(message.encode())

data = client.recv(1024)
print("Accepted from server:", data.decode())

client.close()