""" Server of the Guess application
"""
import socket
import select
import threading
import logging
import random
import operator
import Queue
import struct
import task2_postal


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

		self.clients = {}

		self.connections = [self.server]

		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])
		while True:
			data, address = self.server.recvfrom(4096)
			unpacker = struct.Struct('5s 5s')
			unpacked = unpacker.unpack(data)
			print unpacked

			if unpacked[0] == 'LOGIN':
				if not address in self.clients:
					print "NOT IN CLIENTS"
					self.clients[str(address)] = Queue.Queue
				else:
					print "ALREADY LOGGED IN"

			elif unpacked[0] == 'QUERY':
				print "QUERR"
			self.server.sendto('Hello kliens', address)


if __name__ == '__main__':
	task2_postal.run()
