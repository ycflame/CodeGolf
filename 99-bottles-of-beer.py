f = lambda i: "%d bottle" % i + ("s" if i > 1 else "") + " of beer"
y = lambda i: "Take one down and pass it around," if i != 1 else "Go to the store and buy some more,"
for i in range(99, 0, -1):
    print "%s on the wall, %s." % (f(i), f(i))
    print "%s %s on the wall.\n" % (y(i), f(i - 1 if i > 1 else 99))
