import socket
import host
import task1_calc


class Client(host.Host):
	""" Client class

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
		self.server_addr = (self.config["server"].config["host"],
		                    self.config["server"].config["port"])
		self.logger.info("Finished initializing %s, id: %s", self.__class__.__name__,
		                 self.config['id'])

	def run(self):
		""" Upon thread start
		"""
		message = '''{"a": 1, "b": 2, "o": "+"}'''
		self.client.connect(self.server_addr)
		self.client.sendall(message)
		self.logger.info("Client request sent: %s", message)
		data = self.client.recv(4096)
		self.logger.info("Client recieved response: %s", data)
		self.client.close()


if __name__ == '__main__':
	task1_calc.run()
