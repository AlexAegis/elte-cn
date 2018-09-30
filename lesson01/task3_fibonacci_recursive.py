""" Task 3

Write a function what gives back the nth fibonacci number

Returns:
	void -- output of the fibonacci numbers calculated from 0 to 20
"""


def fibonacci(num):
	""" recursive fibonacci calculation

	Arguments:
		num {int} -- nth iteration of fibonacci

	Returns:
		int -- nth iteration of fibonacci
	"""

	return num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)


for i in range(0, 21):
	print str(i) + ": " + str(fibonacci(i))
