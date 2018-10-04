""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import task3_guess_server
import task3_guess_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task3_guess_server.Server({
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	client_a = task3_guess_client.Client({"id": "a", "server": server})
	client_b = task3_guess_client.Client({"id": "b", "server": server})
	server.start()
	client_a.start()
	time.sleep(1)
	client_b.start()


if __name__ == '__main__':
	run()
