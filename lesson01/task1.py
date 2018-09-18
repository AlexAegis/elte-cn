import this

print "hello world!"

mylist = [1, 5, 6, 3, 4, 7]

for e in sorted(mylist):
    print e


def isEven(i):
    if i % 2 == 0:
        return True
    else:
        return False


print str(isEven(2)) + " " + str(isEven(3))
