""" Server of the Guess application
"""
import socket
import json
import exam
import host
import operator
from collections import namedtuple


class Fairy(host.Host):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- host, portk
		"""
		host.Host.__init__(self, config)
		self.server_addr = (config["host"], config["port"])
		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server.bind(self.server_addr)
		self.connections = [self.server]

		self.logger.info("\t\tFinished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("\t\tStarting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])
		while True:
			data, address = self.server.recvfrom(4096)

			response = {"response": "a"}

			self.logger.info("\t\tGot data: %s", data)
			json_obj = json.loads(data)
			print json_obj

			self.logger.critical("\t\tAsked santa, got this: %s", response["response"])

			self.server.sendto(json.dumps(response), address)


if __name__ == '__main__':
	exam.run()
