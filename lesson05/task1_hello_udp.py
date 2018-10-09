""" Task 1
Create a UDP application what is capable of sending and recieving a hello message
all by itself
"""
import logging
import task1_hello_udp_server
import task1_hello_udp_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("Bootstrapping application")
	server = task1_hello_udp_server.Server({
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})
	client = task1_hello_udp_client.Client({"id": "a", "server": server})
	server.start()
	client.start()


if __name__ == '__main__':
	run()
