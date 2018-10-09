""" Client for the guesser application
"""
import logging
import socket
import time
import threading
import random
import task2_postal


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
		comparisions = ["<", ">"]
		while guess_l is not None and guess_h is not None and guess_l != guess_h:
			guess = random.randint(guess_l, guess_h + 1)
			if guess_l == guess or guess_l == guess or guess_h - guess_l <= 1:
				comparision = "="
			else:
				comparision = random.choice(comparisions)

			self.client.sendall(comparision + " " + str(guess))
			self.logger.info("\tTaken guess between %i and %i, guess is: %s %i", guess_l,
			                 guess_h, comparision, guess)
			data = self.client.recv(16)
			self.logger.info("\tRecieved result of guess: %s", data)

			if data == "yes":
				if comparision == "<":
					guess_h = guess - 1
				elif comparision == ">":
					guess_l = guess + 1
				elif comparision == "=":
					guess_l = guess
					guess_h = guess
			elif data == "no":
				if comparision == "<":
					guess_l = guess
				elif comparision == ">":
					guess_h = guess
			elif data == "win":
				self.logger.info("\t\tHooray, I won! I guessed %i!", guess)
				guess_l = None
				guess_h = None
			elif data == "end":
				self.logger.info("\t\tOof! They game ended me!")
				guess_l = None
				guess_h = None

			time.sleep(1)

		self.client.close()


if __name__ == '__main__':
	task2_postal.run()
