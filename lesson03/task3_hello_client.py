""" this file is meant to run second so before doing
anything it should run file a, unless it's called from file a
"""

import task3_hello
import socket
import threading


class Client(threading.Thread):
	"""[summary]

	Arguments:
		object {[type]} -- [description]
	"""

	def __init__(self, config):
		threading.Thread.__init__(self)
		print "Initializing " + self.class_name()

	def run(self):
		"""test print
		"""
		print "Starting " + self.class_name()
		self.client = socket.socket()

		self.server_addr = ('localhost', 11213)
		self.client.connect(self.server_addr)

		self.client.sendall('Hello server')

		data = self.client.recv(16)

		print data

		self.client.close()

	@classmethod
	def class_name(cls):
		"""test print
		"""

		return cls.__name__


if __name__ == '__main__':
	task3_hello.run()
