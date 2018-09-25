import socket

client = socket.socket()

server_addr = ('localhost', 10000)
client.connect(server_addr)

client.sendall('Hello server')

data = client.recv(16)

print data

client.close()
