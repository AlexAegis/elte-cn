import socket
import host
import datetime
import task1_calc
import json
import time


class Client(host.Host):
	""" Client class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config, messages=[]):
		""" Constructor

		Arguments:
			config {dict} -- server
		"""
		host.Host.__init__(self, config)
		self.client = socket.socket()
		self.server_addr = (self.config["server"].config["host"],
		                    self.config["server"].config["port"])
		self.logger.info("\t\tFinished initializing %s, id: %s",
		                 self.__class__.__name__, self.config['id'])
		self.messages = messages

	def run(self):
		""" Upon thread start
		"""

		self.client.connect(self.server_addr)
		for message in self.messages:
			time.sleep(1)
			self.client.sendall(message)
			self.logger.info("\t\tClient request sent: %s", message)
			data = self.client.recv(4096)
			self.logger.info("\t\tClient recieved response: %s", data)
			result = json.loads(data)

			self.logger.info("\t\t\t\t result of: %s, is: %s", message, result["result"])
		self.client.close()


if __name__ == '__main__':
	task1_calc.run()
