""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import exam_fairy
import exam_santa
import exam_elf


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("\t\tBootstrapping application")

	santa = exam_santa.Santa({
	    "id": "cache",
	    "host": "localhost",
	    "port": 11233,
	    "timeout": 5,
	}, "./exam/destinations.json")

	fairy = exam_fairy.Fairy({
	    "id": "server",
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5,
	    "santa": santa
	})

	elf_a = exam_elf.Elf({"id": "a", "santa": santa, "fairy": fairy})
	elf_b = exam_elf.Elf({"id": "b", "santa": santa, "fairy": fairy})
	elf_c = exam_elf.Elf({"id": "c", "santa": santa, "fairy": fairy})

	santa.start()
	fairy.start()
	elf_a.start()
	elf_b.start()
	elf_c.start()


if __name__ == '__main__':
	run()
