import socket

print socket.gethostname()
print socket.gethostbyname('www.python.org')

for response in socket.getaddrinfo('www.python.org', 'http'):
    print response

for response in socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME):
    print 'lol'
    family, socktype, proto, cannonname, sockaddr = response
    print family, socktype, proto, cannonname, sockaddr
