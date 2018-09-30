""" Task 2

Mark the days of the week from 0 to 6 (Monday to Sunday)
Write a function what gives back when to wake up on that day

On weekdays at '7:00' on weekend at '10:00'. Unless we're on a vacation,
then on weekdays it's '10:00' and on weekend it's 'OFF'

Returns:
	void -- prints out a few examples using the function written
"""


def is_weekend(day):
	""" determines from a day (represented as a number) whether
	it's a day of the weekend or not

	Arguments:
		day {int} -- 0-6, 5 and 6 is weekend

	Returns:
		bool -- weekend or not
	"""

	return day >= 5 & day <= 6


def alarm_clock(day, is_vacation):
	"""outputs the alarm clock setting for that day

	Arguments:
		day {int} -- 0-6, 5 and 6 is weekend
		is_vacation {bool} -- it's a vacation or not

	Returns:
		str -- the setting of the alarm clock for the inputs given
	"""

	if not is_vacation:
		return "7:00" if not is_weekend(day) else "10:00"
	return "10:00" if not is_weekend(day) else "OFF"


print "is_weekend(0): " + str(is_weekend(0))
print "is_weekend(6): " + str(is_weekend(6))

print "alarm_clock(0, False): " + str(alarm_clock(0, False))
print "alarm_clock(6, False): " + str(alarm_clock(6, False))
print "alarm_clock(2, True): " + str(alarm_clock(2, True))
print "alarm_clock(5, True): " + str(alarm_clock(5, True))
