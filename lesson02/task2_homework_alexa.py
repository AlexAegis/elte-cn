""" Task 2 - Alexa-top-1m """

import csv
from itertools import islice
from subprocess import call
import platform


def tail(p_file, number):
	""" Reads a certain amount of lines from the end of the
	file given, using an exponential search for said number of lines.

	Arguments:
			p_file {BufferedIOBase} -- file to get the tail of
			number {int} -- line count

    Returns:
			array<str> -- tail of p_file
    """

	assert number >= 0
	pos, lines = number + 1, []
	while len(lines) <= number:
		try:
			p_file.seek(-pos, 2)
		except IOError:
			p_file.seek(0)
			break
		finally:
			lines = list(p_file)
		pos *= 2
	return lines[-number:]


def head(p_file, number):
	""" Reads a certain number of rows from the begginning of
	the file given, using islice which is implemented in C, so it should be fast

	Arguments:
			p_file {BufferedIOBase} -- file to get the head of
			number {int} -- number of lines to read

    Returns:
			array<str> -- head of p_file
    """

	return list(islice(p_file, number))


with open("./lesson02/top-1m.csv", 'rb') as csv_file:
	HEAD = head(csv_file, 100)
	TAIL = tail(csv_file, 100)
	FILE_READER = csv.reader(HEAD, delimiter=',', dialect='excel')
	for row in FILE_READER:
		print row[0]
		print row[1]

print platform.system()  # Windows

call(["ping", "www.google.com"], shell=True)
