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
		self.fairy_addr = (self.config["fairy"].config["host"],
		                   self.config["fairy"].config["port"])
		self.one_more = False
		self.fairy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.logger.info("\t\tFinished initializing %s, id: %s",
		                 self.__class__.__name__, self.config['id'])
		self.dismissed = False

	def run(self):
		""" Upon thread start
		"""
		self.client.connect(self.santa_addr)
		self.fairy.connect(self.fairy_addr)
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
					self.dismissed = True
					self.logger.critical("\tBoo-hoo!")
					fairy_request = json.dumps({"action": "help"})
					self.fairy.sendto(fairy_request, self.fairy_addr)
					self.logger.info("\t\t\tWent to the fairy!: %s", fairy_request)

					fairy_response_str, address = self.fairy.recvfrom(4096)
					self.logger.info("\t\t\tGot message from the fairy!: %s",
					                 fairy_response_str)
					fairy_response = json.loads(fairy_response_str)
					if fairy_response["response"] == 'nowhere':
						self.logger.critical("\tBoo-hoo-HOO!")
					else:
						self.logger.critical("\tYES!")
						self.one_more = True
						self.dismissed = False
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
