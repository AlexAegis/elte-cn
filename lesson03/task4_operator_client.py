""" this file is meant to run second so before doing
anything it should run file a, unless it's called from file a
"""
import socket
import threading
import task4_operator


class Client(threading.Thread):
	""" Client class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- server
		"""

		threading.Thread.__init__(self)
		print "Initializing " + self.__class__.__name__
		self.config = config
		self.client = socket.socket()
		self.server_addr = (self.config["server"].config["host"],
		                    self.config["server"].config["port"])
		print "Finished initializing " + self.__class__.__name__

	def run(self):
		""" Upon thread start
		"""
		print "Starting " + self.__class__.__name__

		message = '''{"a": 1, "b": 2, "o": "+"}'''

		self.client.connect(self.server_addr)
		self.client.sendall(message)

		print "\tClient sent: " + message
		data = self.client.recv(16)

		print "\tClient recieved: " + data

		self.client.close()


if __name__ == '__main__':
	task4_operator.run()
