""" raw http socket query
"""
import socket

for response in socket.getaddrinfo('www.python.org', 'http'):
	print response

for response in socket.getaddrinfo('www.python.org', 'http', socket.AF_INET,
                                   socket.SOCK_STREAM, socket.IPPROTO_TCP,
                                   socket.AI_CANONNAME):
	family, socktype, proto, cannonname, sockaddr = response
	print family, socktype, proto, cannonname, sockaddr
