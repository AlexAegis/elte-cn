""" this file is meant to run first then it
should run file b unless it's called from file b

Note that an import will run the script, so anything
whats directly in there will run
Also note that this import syntax altough deals with circular
imports, it still lets the first file run twice, as running
the script is not considered as an import
"""

import task3_hello
import socket
import threading


class Server(threading.Thread):
	""" Server class

	Arguments:
		object {[type]} -- [description]
	"""

	def __init__(self, config):
		threading.Thread.__init__(self)
		print "Initializing " + self.class_name()
		self.server = socket.socket()
		self.server_addr = ('localhost', 11213)
		self.server.bind(self.server_addr)

	def run(self):
		"""test print
		"""

		self.server.listen(1)
		connection, client_addr = self.server.accept()
		data = connection.recv(16)

		print data

		connection.sendall('Hello client')

	@classmethod
	def class_name(cls):
		"""test print
		"""

		return cls.__name__


if __name__ == '__main__':
	task3_hello.run()
