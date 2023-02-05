import socket

IP = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)

print(f'Server listening on {IP}:{PORT}')

client_socket, client_address = server_socket.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    client_socket.send(data)

client_socket.close()
server_socket.close()