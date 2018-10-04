""" Task 1
Create a TCP application what is capable of recieving messages from
multiple clients at once, and for every message it replies "OK".
(Use the "select" function)
"""
import logging
import time
import task2_guess_server
import task2_guess_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task2_guess_server.Server({
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	client_a = task2_guess_client.Client({"server": server})
	client_b = task2_guess_client.Client({"server": server})
	server.start()
	client_a.start()
	time.sleep(1)
	client_b.start()


if __name__ == '__main__':
	run()
