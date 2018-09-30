"""Runner file
"""
import task3_hello_server
import task3_hello_client


def run():
	"""
	Run the files
	"""
	server = task3_hello_server.Server({"host": "localhost", "port": 11232})
	client = task3_hello_client.Client({"server": server})

	server.start()
	client.start()


if __name__ == '__main__':
	run()
