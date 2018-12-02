""" Server of the Guess application
"""
import socket
import json
import Queue
import task1_calc
import host


class Server(host.Host):
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

		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)
		self.clients = {}
		self.connections = [self.server]

		self.logger.info("Finished initializing %s", self.__class__.__name__)

	def get_client_by_address(self, address):
		"""Gets the client entry for the given address

		Arguments:
			address {[type]} -- [description]
		"""

		for client in self.clients.values():
			if client["address"] == address:
				yield client

	def is_logged_in(self, address):
		"""Checks if the client who initiated the connection is logged in and has permission

		Arguments:
			address {[type]} -- Address from which the client tries to log in

		Returns:
			[type] -- The logged in client
		"""

		if self.clients and address:
			client = list(self.get_client_by_address(address))
			if client:
				self.logger.info("\t\tClient is logged in %s, permission granted",
				                 client[0])
				return client[0]
			else:
				self.logger.error("\t\tClient is not logged in %s, permission denied",
				                  address)
				return None

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])
		while True:
			data, address = self.server.recvfrom(4096)
			client = self.is_logged_in(address)
			response = {"action": "response", "result": "", "errors": []}
			try:
				self.logger.info("\tIncoming message %s from %s", data, address)
				incoming = json.loads(data)

			except ValueError as error:
				self.logger.exception("\tException raised %s", error)
				response["errors"].append({"error": "exception", "reason": str(error)})

			if not response["result"]:
				response["errors"].append({
				    "error": "no result",
				    "reason": "not valid action and/or arguments"
				})

			self.server.sendto(json.dumps(response), address)


if __name__ == '__main__':
	task1_calc.run()
