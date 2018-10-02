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
import json
from collections import namedtuple
import operator
import logging
import task1_ok


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
		logging.info("Initializing %s", self.__class__.__name__)
		self.config = config
		self.server = socket.socket()
		self.server_addr = (config["host"], config["port"])
		self.server.bind(self.server_addr)
		logging.info("Finished initializing %s", self.__class__.__name__)

	def run(self):
		""" Upon thread start
		"""
		logging.info("Starting %s", self.__class__.__name__)

		self.server.listen(1)
		connection, client_addr = self.server.accept()
		print "client_addr: " + str(client_addr)

		data = connection.recv(32)

		print data
		json_obj = json.loads(
		    data, object_hook=lambda d: namedtuple('x', d.keys())(*d.values()))
		print json_obj

		result = self.eval(json_obj.a, json_obj.o, json_obj.b)

		print "\tServer recieved: " + data

		connection.sendall(str(result))

		print "\tServer sent: " + str(result)

	@classmethod
	def get_operator_fn(cls, opr):
		""" returns the operator function from a string

		Arguments:
			opr {str} -- operator as a string

		Returns:
			function -- [description]
		"""

		return {
		    '+': operator.add,
		    '-': operator.sub,
		    '*': operator.mul,
		    '/': operator.div,
		    '%': operator.mod,
		    '^': operator.xor,
		}[opr]

	@classmethod
	def eval(cls, op1, opr, op2):
		"""evaluates the two operands with the operator

		Arguments:
			op1 {str} -- first operand
			opr {str} -- operator to be applied
			op2 {str} -- second operand

		Returns:
			int -- result
		"""

		op1, op2 = int(op1), int(op2)
		return cls.get_operator_fn(opr)(op1, op2)


if __name__ == '__main__':
	task1_ok.run()
