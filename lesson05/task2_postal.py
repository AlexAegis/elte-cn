""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import task2_postal_server
import task2_postal_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task2_postal_server.Server({
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	client_a = task2_postal_client.Client({"id": "a", "server": server})
	"""client_b = task1_postal_client.Client({"id": "b", "server": server})
	client_c = task1_postal_client.Client({"id": "c", "server": server})"""
	server.start()
	client_a.start()
	"""time.sleep(0.4)
	client_b.start()
	time.sleep(0.4)
	client_c.start()"""


if __name__ == '__main__':
	run()
