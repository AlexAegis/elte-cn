import socket

server = socket.socket()

server_addr = ('localhost', 10000)

server.bind(server_addr)

server.listen(1)

connection, client_addr = server.accept()

data = connection.recv(16)

print data

connection.sendall('Hello client')
