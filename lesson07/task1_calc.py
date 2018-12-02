""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import task1_calc_server
import task1_calc_cache
import task1_calc_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task1_calc_server.Server({
	    "id": "server",
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})

	cache = task1_calc_cache.Cache({
	    "id": "cache",
	    "host": "localhost",
	    "port": 11233,
	    "timeout": 5,
	    "server": server
	})

	client_a = task1_calc_client.Client({"id": "a", "server": cache})

	#client_b = task3_guess_client.Client({"id": "b", "server": server})
	#client_c = task3_guess_client.Client({"id": "c", "server": server})
	server.start()
	cache.start()
	client_a.start()


if __name__ == '__main__':
	run()
