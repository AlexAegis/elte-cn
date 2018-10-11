""" Client for the guesser application
"""
import socket
import json
import host
import task2_postal


class Client(host.Host):
	""" Client class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor of the guesser client

		Arguments:
			config {dict} -- server, id
		"""

		host.Host.__init__(self, config)
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
		self.login()
		self.send('a', "something for myself")
		self.send('b', "something for b")
		self.query()

	def login(self):
		"""Initiates a login to the server
		"""

		self.logger.info("\tAbout to log in to server")
		message = {"action": "login", "id": self.config["id"]}
		self.client.sendto(json.dumps(message), self.server_addr)
		data, address = self.client.recvfrom(4096)
		self.logger.info("\tLogged in to server %s, receieved result: %s", address,
		                 data)

	def send(self, recipient, message):
		"""Sends a message to another recipient throught he server

		Arguments:
			recipient {[type]} -- The destination of the message
			message {string} -- content of the message
		"""

		self.logger.info("\tAbout to send a message to: %s", recipient)
		message = {"action": "send", "recipient": recipient, "message": message}
		self.client.sendto(json.dumps(message), self.server_addr)
		data, address = self.client.recvfrom(4096)
		self.logger.info("\tMessage (%s) sent to server %s, receieved result: %s",
		                 message, address, data)

	def query(self):
		""" Queries the inbox of the client
		"""
		self.logger.info("\tAbout query the inbox")
		message = {"action": "query"}
		self.client.sendto(json.dumps(message), self.server_addr)
		data, address = self.client.recvfrom(4096)
		self.logger.info("\tMessage (%s) sent to server %s, receieved result: %s",
		                 message, address, data)
		#message = self.packer.pack("QUERY", "EMPTY")
		#print message
		#self.client.sendto(message, self.server_addr)
		#data, address = self.client.recvfrom(4096)
		#print data


if __name__ == '__main__':
	task2_postal.run()
