""" Task 1
Write a function what returns from a given
year whether its a leap year or not.

A year is a leap year if 4 is it's divisor
but not if it's also divisible by 100 except
if it's not also divisible by 400

Example leap years: 1992,1996,2000,2400
Non leap years: 1993, 1900.


Returns:
	void -- prints the result of is_leap_year for multiple examples
"""


def is_leap_year(year):
	""" Determines from a year whether it's a leap year or not

	Arguments:
		year {int} -- year as an integer

	Returns:
		bool -- is a leap year or not
	"""

	return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


print "year: " + "is leap year"
print "1992: " + str(is_leap_year(1992))
print "1996: " + str(is_leap_year(1996))
print "2000: " + str(is_leap_year(2000))
print "2400: " + str(is_leap_year(2400))

print "1993: " + str(is_leap_year(1993))
print "1900: " + str(is_leap_year(1900))

print "2004: " + str(is_leap_year(2004))
print "1903: " + str(is_leap_year(1903))
print "2005: " + str(is_leap_year(2005))
