""" this file is meant to run first then it
should run file b unless it's called from file b

Note that an import will run the script, so anything
whats directly in there will run
Also note that this import syntax altough deals with circular
imports, it still lets the first file run twice, as running
the script is not considered as an import
"""
import socket
import threading
import task3_hello


class Server(threading.Thread):
	""" Server class

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Cosntructor

		Arguments:
			config {dict} -- host, port
		"""

		threading.Thread.__init__(self)
		print "Initializing " + self.__class__.__name__
		self.config = config
		self.server = socket.socket()
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)
		print "Finished initializing " + self.__class__.__name__

	def run(self):
		""" Upon thread start
		"""
		print "Starting " + self.__class__.__name__

		message = 'Hello client'
		self.server.listen(1)
		connection, client_addr = self.server.accept()
		print "client_addr: " + str(client_addr)
		data = connection.recv(16)
		print "\tServer recieved: " + data
		connection.sendall(message)

		print "\tServer sent: " + message


if __name__ == '__main__':
	task3_hello.run()
