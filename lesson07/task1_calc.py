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
	logging.info("\t\tBootstrapping application")
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

	client_a = task1_calc_client.Client({
	    "id": "a",
	    "server": cache
	}, [
	    '{"a": 1, "b": 2, "o": "+"}',
	    '{"a": 1, "b": 2, "o": "+"}',
	    '{"a": 2, "b": 2, "o": "+"}',
	    '{"a": 1, "b": 4, "o": "*"}',
	    '{"a": 2, "b": 2, "o": "+"}',
	    '{"a": 2, "b": 2, "o": "/"}',
	    '{"a": 1, "b": 2, "o": "-"}',
	])

	client_b = task1_calc_client.Client({
	    "id": "b",
	    "server": cache
	}, [
	    '{"a": 2, "b": 2, "o": "/"}',
	    '{"a": 1, "b": 2, "o": "-"}',
	])

	server.start()
	cache.start()
	client_a.start()
	client_b.start()


if __name__ == '__main__':
	run()
