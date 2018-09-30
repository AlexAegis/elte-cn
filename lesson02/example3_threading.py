""" Example 3
Threading
"""

import threading
import time


class MyThread(threading.Thread):
	""" Example thread class extending the base thread class

	Arguments:
		threading {[type]} -- [description]
	"""

	def run(self):
		""" Run the thread and log it
		"""

		print "{} started!".format(self.getName())  # Thread-x started!
		time.sleep(2)  # Pretend to work for a second
		print "{} finished!".format(self.getName())  # "Thread-x finished!"


if __name__ == '__main__':
	for x in range(50):  # Four times...
		mythread = MyThread(name="Thread-{}".format(
		    x + 1))  # ...Instantiate a thread and pass a unique ID to it
		mythread.start()  # ...Start the thread
		time.sleep(.5)  # ...Wait 0.6 seconds before starting another
