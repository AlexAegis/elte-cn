import socket
import host
import datetime
import exam
import json
import time
import random


class Elf(host.Host):
	""" Elf class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- server
		"""
		host.Host.__init__(self, config)
		self.client = socket.socket()
		self.santa_addr = (self.config["santa"].config["host"],
		                   self.config["santa"].config["port"])
		self.logger.info("\t\tFinished initializing %s, id: %s",
		                 self.__class__.__name__, self.config['id'])
		self.dismissed = False

	def run(self):
		""" Upon thread start
		"""
		self.client.connect(self.santa_addr)
		while not self.dismissed:

			request = {"action": "where"}
			self.client.sendall(json.dumps(request))
			data = self.client.recv(4096)
			result = json.loads(data)
			self.logger.info("\t\tClient recieved result for login: %s", data)
			if result['result'] == 'nowhere':
				self.logger.error('no more destination..')
				self.dismissed = True
			else:
				time.sleep(random.randint(1, 11))
				response = {"action": "done"}
				self.client.sendall(json.dumps(response))
				data = self.client.recv(4096)
				result = json.loads(data)

				if result['result'] == 'good_job':
					self.logger.info("\tHooray!")
				elif result['result'] == 'dismissed':
					self.logger.critical("\tFML!")
					self.dismissed = True
		"""
		for message in self.messages:
			time.sleep(1)
			self.client.sendall(message)
			self.logger.info("\t\tClient request sent: %s", message)
			data = self.client.recv(4096)
			self.logger.info("\t\tClient recieved response: %s", data)
			result = json.loads(data)

			self.logger.info("\t\t\t\t result of: %s, is: %s", message, result["result"])
		
		"""
		self.client.close()


if __name__ == '__main__':
	exam.run()
