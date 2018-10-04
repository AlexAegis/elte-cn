""" Server of the Guess application
"""
import socket
import select
import threading
import logging
import random
import operator
import task3_guess


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
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setblocking(0)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)

		self.connections = [self.server]
		self.number = random.randint(1, 101)
		self.logger.info("Random number generated: %i", self.number)
		self.ops = {"<": operator.lt, ">": operator.gt, "=": operator.eq}
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
				self.handle_exceptionals(exceptionals)

			except KeyboardInterrupt:
				self.logger.info("Exit")
				for connection in self.connections:
					connection.close()
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

	def handle_exceptionals(self, exceptionals):
		""" Handle the exeptional sockets

		Arguments:
			exceptionals {[type]} -- [description]
		"""

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
			answer = "NaN"
			try:
				if self.number is not None:
					if self.ops[data.split()[0]](self.number, int(data.split()[1])):
						if data.split()[0] == "=":
							answer = "win"
							self.number = None
						else:
							answer = "yes"
					else:
						answer = "no"
				else:
					answer = "end"
			except ValueError:
				self.logger.error("\tClient's guess is not an int, instead: %s", data)
			self.logger.info(
			    "\t%s recieved %s, confirming by returning message: %s to %s",
			    self.__class__.__name__, data, answer, sock.getpeername())
			sock.sendall(answer)
		else:
			self.logger.info("no data, closing connection %s", sock.getpeername())
			self.connections.remove(sock)
			sock.close()

	def broadcast(self, sock):
		""" Broadcast the winner among the participants

		Arguments:
			sock {[type]} -- The winner
		"""

		for connection in self.connections:
			if connection != sock:
				connection.sendall("end")
				connection.close()

		self.connections = [sock]


if __name__ == '__main__':
	task3_guess.run()
