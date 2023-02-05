import socket

IP = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

data = b'Hello, Server!'
client_socket.send(data)

response = client_socket.recv(1024)
print(f'Received: {response.decode()}')

client_socket.close()