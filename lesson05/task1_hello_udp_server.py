""" Server of the Guess application
"""
import socket
import select
import threading
import logging
import random
import operator
import task1_hello_udp


class Server(threading.Thread):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- host, port
		"""

		threading.Thread.__init__(self)
		self.logger = logging.getLogger(self.__class__.__name__)
		self.logger.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)

		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])

		data, address = self.server.recvfrom(4096)

		print "Incoming message from", address
		print "Message:", data

		self.server.sendto('Hello kliens', address)
		#self.server.listen(5)

		#self.server.close()


if __name__ == '__main__':
	task1_hello_udp.run()
