""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import exam_santa_server
import exam_santa_cache
import exam_santa_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("\t\tBootstrapping application")
	server = exam_santa_server.Server({
	    "id": "server",
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})

	cache = exam_santa_cache.Cache({
	    "id": "cache",
	    "host": "localhost",
	    "port": 11233,
	    "timeout": 5,
	    "server": server
	})

	client_a = exam_santa_client.Client({
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

	client_b = exam_santa_client.Client({
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
