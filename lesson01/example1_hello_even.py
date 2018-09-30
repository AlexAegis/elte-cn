""" Task 0

examples

Returns:
	void -- output of the is_even function for two examples
	and the docstring of said function
"""

MY_LIST = [1, 5, 6, 3, 4, 7]

for e in sorted(MY_LIST):
	print e


def is_even(i):
	""" checks if a number is even or not

	Arguments:
		i {int} -- number to check

    Returns:
		bool -- is 'i' even or not
    """

	return bool(i % 2 == 0)


print str(is_even(2)) + " " + str(is_even(3))

help(is_even)
