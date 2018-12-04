""" Server of the Guess application
"""
import socket
import json
import exam_santa
import host
import operator
import random
from collections import namedtuple


class Server(host.Host):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config, destinations):
		""" Constructor

		Arguments:
			config {dict} -- host, portk
		"""
		host.Host.__init__(self, config)
		self.server_addr = (config["host"], config["port"])
		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server.bind(self.server_addr)
		self.connections = [self.server]
		self.destinations = destinations
		self.logger.info("\t\tFinished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("\t\tStarting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])
		while True:
			data, address = self.server.recvfrom(4096)

			response = {"action": "response", "result": "hello", "errors": []}

			if data:
				request = json.loads(data)
				self.logger.info("\t\tGot data: %s", data)
				if request['action'] == 'where':
					response["result"] = random.choice(self.destinations)
					self.destinations.remove(response["result"])
					self.logger.critical("\t\tresponse: %s", response["result"])

				if request['action'] == 'done':
					self.logger.info("\tCLIENT IS DONE")
			self.server.sendto(json.dumps(response), address)


if __name__ == '__main__':
	exam_santa.run()
