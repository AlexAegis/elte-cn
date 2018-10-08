""" Task 2 - Alexa-top-1m """

import csv
import json
import threading
import platform
import datetime
from itertools import islice
from subprocess import PIPE, Popen
from multiprocessing.pool import ThreadPool


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


def ping(row):
	""" Runs the ping command a certain times

	Arguments:
		identification {int} -- [description]
		target {[type]} -- [description]

	Returns:
		[type] -- [description]
	"""

	ping_iter_arg = '-n'
	if platform.system() == 'Windows':
		ping_iter_arg = '-n'
	elif platform.system() == 'Linux':
		ping_iter_arg = '-c'

	pipe = Popen(["ping", ping_iter_arg, "2", row[1]], shell=True, stdout=PIPE)
	pipe.wait()
	return (row[1], "Rank: " + str(row[0]) + pipe.communicate()[0].decode())


def traceroute(row):
	""" runs a traceroute for the given target

	Arguments:
		identification {[type]} -- [description]
		target {[type]} -- [description]
	"""
	traceroute_executable = 'tracert'
	if platform.system() == 'Windows':
		traceroute_executable = 'tracert'
	elif platform.system() == 'Linux':
		traceroute_executable = 'traceroute'

	traceroute_hops_arg = '-h'
	if platform.system() == 'Windows':
		traceroute_hops_arg = '-h'
	elif platform.system() == 'Linux':
		traceroute_hops_arg = '-m'

	pipe = Popen([traceroute_executable, traceroute_hops_arg, "3", row[1]],
	             shell=True,
	             stdout=PIPE)
	pipe.wait()
	return (row[1], "Rank: " + str(row[0]) + pipe.communicate()[0].decode())


def query(command, entries):
	""" Runs the command on each entry in entries and
	prints it out in a json file

	Arguments:
		command {function} -- the command to run
		entries {[type]} -- [description]

	Returns:
		[array<str>] -- all the results of the pings
	"""

	pool = ThreadPool(processes=200)
	results = pool.map(command, entries)

	result_pings = {
	    "date": str(datetime.datetime.now().strftime("%Y%m%d")),
	    "system": str(platform.system()),
	    command.__name__ + 's': []
	}
	for target, ping_output in results:
		entry = {}
		entry['target'] = target
		entry['output'] = ping_output
		result_pings[command.__name__ + 's'].append(entry)

	with open(command.__name__ + "s.json", "w") as write_file:
		json.dump(
		    result_pings,
		    write_file,
		    indent=4,
		    ensure_ascii=True,
		    separators=(',', ': '))

	pool.close()
	pool.join()
	return results


with open("./lesson02/top-1m.csv", 'rb') as csv_file:
	HEAD = head(csv_file, 100)
	TAIL = tail(csv_file, 100)
	query(ping, csv.reader(HEAD + TAIL, delimiter=',', dialect='excel'))
	query(traceroute, csv.reader(HEAD + TAIL, delimiter=',', dialect='excel'))
