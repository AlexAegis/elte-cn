""" Server of the Guess application
"""
import socket
import select
import threading
import logging
import operator
import task1_calc
import host
import datetime
import colorer


class Cache(host.Host):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- host, port
		"""
		host.Host.__init__(self, config)
		self.server_addr = (config["host"], config["port"])
		self.backend_addr = (config["server"].config["host"],
		                     config["server"].config["port"])
		self.server = socket.socket()
		self.server.setblocking(0)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(self.server_addr)

		self.backend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.connections = [self.server]

		self.cache = {}

		self.finished = False
		#self.ops = {"<": operator.lt, ">": operator.gt, "=": operator.eq}

		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])

		self.server.listen(5)
		self.backend.connect(self.backend_addr)

		while not self.finished:
			try:
				readables, writables, exceptionals = select.select(
				    self.connections, [], self.connections, self.config["timeout"])

				if not (readables or writables or exceptionals):
					continue

				self.handle(readables)
				self.handle_exceptionals(exceptionals)

			except KeyboardInterrupt:
				self.logger.error("Exit")
				for connection in self.connections:
					connection.close()

				self.connections = []

		self.logger.info("Game Ended. Closing...")
		self.server.close()

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

	def handle_exceptionals(self, exceptionals):
		""" Handle the exeptional sockets

		Arguments:
			exceptionals {[type]} -- [description]
		"""

		for sock in exceptionals:
			self.logger.warning("Exceptional connection closed %s", sock.getpeername())
			self.connections.remove(sock)
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

		data = sock.recv(4096)
		data = data.strip()

		if data:
			answer = None

			if (data in self.cache):
				self.logger.warn("\t\tcache exists for: %s, cache is: %s", data,
				                 self.cache[data])
				if (self.cache[data]["created"] >
				    datetime.datetime.now() - datetime.timedelta(seconds=4)):
					self.logger.warn("\t\tcache valid")
					answer = self.cache[data]["result"]
				else:
					self.logger.error("\t\tcache invalid. Invalidating.")
					del self.cache[data]

			if (answer is None):
				self.backend.sendto(data, self.backend_addr)
				self.logger.info("\t\t\tCache sent message to server: %s", data)
				answer, address = self.backend.recvfrom(4096)

				self.cache[data] = {"result": answer, "created": datetime.datetime.now()}
				self.logger.info("\t\t\tCache recieved message from server: %s", answer)

			sock.sendall(answer)

		else:
			self.logger.info("\t\tNo data, closing connection for %s",
			                 sock.getpeername())
			self.connections.remove(sock)
			sock.close()
			if len(self.connections) == 1:
				self.finished = True
				self.backend.close()


if __name__ == '__main__':
	task1_calc.run()
