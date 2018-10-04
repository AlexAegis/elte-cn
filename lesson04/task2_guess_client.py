""" Client for the guesser application
"""
import logging
import socket
import time
import threading
import random
import task2_guess


class Client(threading.Thread):
	""" Client class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor of the guesser client

		Arguments:
			config {dict} -- server, id
		"""

		threading.Thread.__init__(self)
		self.logger = logging.getLogger(self.__class__.__name__ + "_" + config["id"])
		self.logger.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

		guess_l = 0
		guess_h = 100

		while guess_l != guess_h:
			guess = random.randint(guess_l, guess_h + 1)
			self.client.sendall(str(guess))
			self.logger.info("\tTaken guess between %i and %i, guess is: %i", guess_l,
			                 guess_h, guess)
			data = self.client.recv(16)
			self.logger.info("\tRecieved result of guess: %s", data)

			if data == "<":
				guess_l = guess
			elif data == ">":
				guess_h = guess
			elif data == "=":
				guess_l = guess
				guess_h = guess
			time.sleep(1)

		self.client.close()


if __name__ == '__main__':
	task2_guess.run()
