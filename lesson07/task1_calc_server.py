""" Server of the Guess application
"""
import socket
import json
import task1_calc
import host
import operator


class Server(host.Host):
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

		self.logger.info("Finished initializing %s", self.__class__.__name__)

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

	def run(self):
		""" Upon thread start
		"""
		self.logger.info("Starting %s Listening on port: %s ",
		                 self.__class__.__name__, self.config["port"])
		while True:
			data, address = self.server.recvfrom(4096)

			response = {"action": "response", "result": "hello", "errors": []}
			"""
			try:
				self.logger.info("\tIncoming message %s from %s", data, address)
				incoming = json.loads(data)

			except ValueError as error:
				self.logger.exception("\tException raised %s", error)
				response["errors"].append({"error": "exception", "reason": str(error)})

			if not response["result"]:
				response["errors"].append({
				    "error": "no result",
				    "reason": "not valid action and/or arguments"
				})
			"""

			self.server.sendto(json.dumps(response), address)


if __name__ == '__main__':
	task1_calc.run()
