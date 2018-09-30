""" Task 1
a) Print out the result of the socket.gethostname() function
b) Call the gethostbyname() and the gethostbyname_ex()
functions for these addresses:
- 'homer', 'www.python.org', 'inf.elte.hu'
c) Using the gethostbyaddr() function query the hostname
of the following IP addresses:
- '157.181.161.79', '185.43.207.92'
"""

import socket

# a)
print "socket.gethostname(): " + socket.gethostname()

# b)
try:
	print "socket.gethostbyname('homer'): " + socket.gethostbyname('homer')
except socket.gaierror as error:
	print "socket.gethostbyname('homer') is not accessible: " + str(error)

print "socket.gethostbyname('www.python.org'): " + socket.gethostbyname(
    'www.python.org')
print "socket.gethostbyname('inf.elte.hu'): " + socket.gethostbyname(
    'inf.elte.hu')
try:
	print "socket.gethostbyname_ex('homer'): " + str(
	    socket.gethostbyname_ex('homer'))
except socket.gaierror as error:
	print "socket.gethostbyname_ex('homer') is not accessible: " + str(error)

print "socket.gethostbyname_ex('www.python.org'): " + str(
    socket.gethostbyname_ex('www.python.org'))
print "socket.gethostbyname_ex('inf.elte.hu'): " + str(
    socket.gethostbyname_ex('inf.elte.hu'))

# c)
print "socket.gethostbyaddr('157.181.161.79'): " + str(
    socket.gethostbyaddr('157.181.161.79'))
print "socket.gethostbyaddr('185.43.207.92'): " + str(
    socket.gethostbyaddr('185.43.207.92'))
