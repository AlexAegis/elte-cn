"""Runner file
"""
import task4_operator_server
import task4_operator_client


def run():
	"""
	Run the files
	"""
	server = task4_operator_server.Server({"host": "localhost", "port": 11232})
	client = task4_operator_client.Client({"server": server})

	server.start()
	client.start()


if __name__ == '__main__':
	run()
