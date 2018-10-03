""" this file is meant to run second so before doing
anything it should run file a, unless it's called from file a
"""
import logging
import socket
import time
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
		self.logger = logging.getLogger(self.__class__.__name__)
		self.logger.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.server_addr = (self.config["server"].config["host"],
		                    self.config["server"].config["port"])
		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.client.connect(self.server_addr)
		self.logger.info(
		    "Starting %s, Connected to server on port: %s, Listening from port: %s",
		    self.__class__.__name__, self.server_addr[1],
		    self.client.getsockname()[1])

		message = '''Hello!'''

		for i in range(0, 5):
			self.client.sendall(message)
			self.logger.info("\tSent: %s", message)
			data = self.client.recv(16)
			self.logger.info("\tRecieved: %s", data)
			time.sleep(2)

		self.client.close()


if __name__ == '__main__':
	task1_ok.run()
