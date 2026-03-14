# Problem 1.5, Page 5 — Division
# Label: exr:div
# An Introduction to the Analysis of Algorithms (4th Edition)

import sys

def division(x, y):
    q = 0
    r = x
    print("q =", 0)
    print("r =", x)
    while y <= r:
        r = r - y
        q = q + 1
        print("q =", q)
        print("r =", r)
    print("%d = %d x %d + %d" % (x, q, y, r))

division(int(sys.argv[1]), int(sys.argv[2]))
