""" Host class
"""

import threading
import logging


class Host(threading.Thread):
	""" Server

	Arguments:
		threading {Thread} -- runnable
	"""

	def __init__(self, config):
		""" Constructor

		Arguments:
			config {dict} -- host, port
		"""

		threading.Thread.__init__(self)
		self.logger = logging.getLogger(self.__class__.__name__ + "_" + config["id"])
		self.config = config
		self.running = True
		self.logger.info("Initializing %s, id: %s", self.__class__.__name__,
		                 self.config["id"])
