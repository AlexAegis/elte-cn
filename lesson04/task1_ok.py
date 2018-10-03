""" Task 1
Create a TCP application what is capable of recieving messages from
multiple clients at once, and for every message it replies "OK".
(Use the "select" function)
"""
import logging
import task1_ok_server
import task1_ok_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task1_ok_server.Server({"host": "localhost", "port": 11232})
	client = task1_ok_client.Client({"server": server})

	server.start()
	client.start()


if __name__ == '__main__':
	run()
