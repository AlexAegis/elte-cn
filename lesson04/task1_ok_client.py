""" this file is meant to run second so before doing
anything it should run file a, unless it's called from file a
"""
import logging
import socket
import threading
import task1_ok


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
		logging.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.client = socket.socket()
		self.server_addr = (self.config["server"].config["host"],
		                    self.config["server"].config["port"])
		logging.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		logging.info("Starting %s", self.__class__.__name__)

		message = '''{"a": 1, "b": 2, "o": "+"}'''

		self.client.connect(self.server_addr)
		self.client.sendall(message)

		print "\tClient sent: " + message
		data = self.client.recv(16)

		print "\tClient recieved: " + data

		self.client.close()


if __name__ == '__main__':
	task1_ok.run()
