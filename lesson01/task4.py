import this


def f(n):
    if n <= 1:
        return n
    else:
        return(f(n-1) + f(n-2))


print "0: " + str(f(0))
print "1: " + str(f(1))
print "2: " + str(f(2))
print "3: " + str(f(3))
print "4: " + str(f(4))
print "5: " + str(f(5))
print "6: " + str(f(6))
