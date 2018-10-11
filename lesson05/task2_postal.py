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
	    "id": "s",
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	client_a = task2_postal_client.Client({"id": "a", "server": server})
	client_b = task2_postal_client.Client({"id": "b", "server": server})
	client_c = task2_postal_client.Client({"id": "c", "server": server})
	server.start()
	client_a.start()
	client_a.login()
	client_a.send('a', "something for myself")
	client_a.send('b', "something for b")
	client_a.query()
	time.sleep(0.4)
	client_b.start()
	client_b.login()
	client_b.query()
	time.sleep(0.4)
	client_c.start()
	client_c.login()
	client_c.send('a', 'something for a from c')
	client_b.send('a', 'something for a from b')
	client_a.query()
	client_c.send('b', 'something for b from c')


if __name__ == '__main__':
	run()
