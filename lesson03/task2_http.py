""" Task 2

a) Query the 'http' informations of 'www.python.org'

b) Query the 'http' servers name of 'www.inf.elte.hu'
with the name flag 'AI_CANNONNAME'
"""
import socket
# a)
for response in socket.getaddrinfo('www.python.org', 'http'):
	print response
# b)
for response in socket.getaddrinfo('www.inf.elte.hu', 'http', socket.AF_INET,
                                   socket.SOCK_STREAM, socket.IPPROTO_TCP,
                                   socket.AI_CANONNAME):
	family, socktype, proto, cannonname, sockaddr = response
	print family, socktype, proto, cannonname, sockaddr
