# Problem 10.6, Page 281 — Fibonacci
# Label: exr:fib-program
# An Introduction to the Analysis of Algorithms (4th Edition)

import numpy as np
import sys

core = np.array([[1,1],[1,0]])

#numpy is a very nice library, so this only takes 3 lines!
def fib(n):#return the nth fibonacci number
    if n in [0,1]: return n
    return np.linalg.matrix_power(core,n-1)[0][0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('fib.py expected at least 1 additional input.')
    else:
        args = sys.argv[1:]
        try:
            args = [int(arg) for arg in args]
        except:
            print('All fib.py inputs should be non-negative integers.')
        else:
            if all([arg>=0 for arg in args]):
                for arg in args:
                    print(('f('+str(arg)+')').rjust(10),':',fib(arg))
            else:
                print('All fib.py inputs should be non-negative integers.')