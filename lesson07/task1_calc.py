""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import task1_calc_server
import task1_calc_cache


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task1_calc_server.Server({
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	#client_a = task3_guess_client.Client({"id": "a", "server": server})
	#client_b = task3_guess_client.Client({"id": "b", "server": server})
	#client_c = task3_guess_client.Client({"id": "c", "server": server})
	server.start()
	#client_a.start()


if __name__ == '__main__':
	run()
