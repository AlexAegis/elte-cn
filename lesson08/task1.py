"""Coding

py -2.7 .\lesson08\task1.py NRZ-L 110011
py -2.7 .\lesson08\task1.py RZ 110011
py -2.7 .\lesson08\task1.py MAN 110011
py -2.7 .\lesson08\task1.py DIFF-MAN 110011
"""

import sys

coding = sys.argv[1]
code = sys.argv[2]
result = []

prev_bit = None
current_voltage = 0
for bit in code:
	print "char: " + str(bit)
	if prev_bit == None:
		current_voltage = int(bit)
	prev_voltage = current_voltage
	if coding == "NRZ-L":

		if prev_bit != None and prev_bit != bit:
			"""change happened"""
			current_voltage = int(bit)
			prev_voltage = current_voltage

	elif coding == "RZ":
		if bit == "1":
			prev_voltage = 1
		current_voltage = 0

	elif coding == "MAN":
		if bit == "0":
			prev_voltage = 0
			current_voltage = 1
		elif bit == "1":
			prev_voltage = 1
			current_voltage = 0

	elif coding == "DIFF-MAN":
		if bit == "0":
			prev_voltage = 1 - prev_voltage
		current_voltage = 1 - prev_voltage

	result.append((prev_voltage, current_voltage))
	prev_bit = bit

print result