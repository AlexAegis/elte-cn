""" this file is meant to run first then it
should run file b unless it's called from file b

Note that an import will run the script, so anything
whats directly in there will run
Also note that this import syntax altough deals with circular
imports, it still lets the first file run twice, as running
the script is not considered as an import
"""
import socket
import select
import threading
import json
from collections import namedtuple
import operator
import logging
import task1_ok


class Server(threading.Thread):
	""" Server class

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
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setblocking(0)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)

		self.connections = [self.server]
		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])

		self.server.listen(5)

		while True:
			try:
				readables, writables, exceptionals = select.select(
				    self.connections, [], self.connections, self.config["timeout"])

				if not (readables or writables or exceptionals):
					continue

				self.handle(readables)
				self.handleExceptionals(exceptionals)

			except KeyboardInterrupt:
				self.logger.info("Exit")
				for c in self.connections:
					c.close()
				self.connections = []

	def handle(self, readables):
		"""[summary]

		Arguments:
			readables {[type]} -- [description]
		"""

		for sock in readables:
			if sock is self.server:
				self.create(sock)
			else:
				self.read(sock)

	def handleExceptionals(self, exceptionals):
		for sock in exceptionals:
			self.logger.warning("Exceptional connection closed %s", sock.getpeername())
			self.inputs.remove(sock)
			sock.close()

	def create(self, sock):
		"""[summary]

		Arguments:
			sock {[type]} -- [description]
		"""

		connection, address = sock.accept()
		self.logger.info("connection created from %s", address)
		connection.setblocking(0)
		self.connections.append(connection)

	def read(self, sock):
		"""[summary]

		Arguments:
			sock {[type]} -- [description]
		"""

		data = sock.recv(1024)
		data = data.strip()

		if data:
			answer = "OK"
			self.logger.info("%s recieved %s, confirming by returning message: %s to %s",
			                 self.__class__.__name__, data, answer, sock.getpeername())
			sock.sendall(answer)
		else:
			self.logger.info("no data, closing connection %s", sock.getpeername())
			self.connections.remove(sock)
			sock.close()


if __name__ == '__main__':
	task1_ok.run()
