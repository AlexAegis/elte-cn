""" Server of the Guess application
"""
import socket
import select
import threading
import logging
import operator
import exam
import host
import datetime
import colorer
import json
import time
import random


class Santa(host.Host):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config, destinations_file):
		""" Constructor

		Arguments:
			config {dict} -- host, port
		"""
		host.Host.__init__(self, config)
		self.server_addr = (config["host"], config["port"])

		self.server = socket.socket()
		self.server.setblocking(0)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(self.server_addr)

		with open(destinations_file) as destinations:
			self.destinations = json.load(destinations)
		self.connections = [self.server]
		self.tasks = {}
		self.cache = {}

		self.finished = False

		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])

		self.server.listen(5)

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
			request = json.loads(data)
			response = {"action": "response", "result": "hello", "errors": []}

			self.logger.info("\t\tGot data: %s", data)
			if request['action'] == 'where' or request['action'] == 'help_request':
				if self.destinations:
					dest, present = random.choice(list(self.destinations.items()))
					response["result"] = dest
					self.tasks[sock] = (response["result"], datetime.datetime.now())
					del self.destinations[dest]
				else:
					response["result"] = "nowhere"

			if request['action'] == 'done':
				if sock in self.tasks:
					client, issued_at = self.tasks[sock]
					if issued_at < datetime.datetime.now() - datetime.timedelta(seconds=6):
						response["result"] = "dismissed"
					else:
						response["result"] = "good_job"

				self.logger.info("\tCLIENT IS DONE")

			self.logger.critical("\t\tresponse: %s", response["result"])

			sock.sendall(json.dumps(response))

		else:
			self.logger.info("\t\tNo data, closing connection for %s",
			                 sock.getpeername())
			self.connections.remove(sock)
			sock.close()
			if len(self.connections) == 1:
				self.finished = True


if __name__ == '__main__':
	exam.run()
