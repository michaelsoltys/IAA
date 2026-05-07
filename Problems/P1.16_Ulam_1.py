# Problem 1.16, Page 10 — Ulam
# Label: exr:ulam
# An Introduction to the Analysis of Algorithms (4th Edition)

import sys

def ulam(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

ulam(int(sys.argv[1]))
print(1)
