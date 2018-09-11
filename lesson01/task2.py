import this

# Leap year 4 is a divisor, but not with 100, unless with 400

def isLeapYear(i):
    return (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0)

print "1903: " + str(isLeapYear(1903))
print "2004: " + str(isLeapYear(2004))
print "2005: " + str(isLeapYear(2005))
print "1900: " + str(isLeapYear(1900))
print "1903: " + str(isLeapYear(1903))
print "2000: " + str(isLeapYear(2000))
