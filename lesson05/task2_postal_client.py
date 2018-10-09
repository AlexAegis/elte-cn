""" Client for the guesser application
"""
import logging
import socket
import time
import threading
import struct
import task2_postal


class Client(threading.Thread):
	""" Client class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor of the guesser client

		Arguments:
			config {dict} -- server, id
		"""

		threading.Thread.__init__(self)
		self.logger = logging.getLogger(self.__class__.__name__ + "_" + config["id"])
		self.logger.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

		packer = struct.Struct('s s')
		message = packer.pack("QUERY", "EMPTY")
		self.client.sendto(message, self.server_addr)
		data, address = self.client.recvfrom(4096)
		print data


if __name__ == '__main__':
	task2_postal.run()
