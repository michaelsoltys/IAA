# Algorithm 9, Page 24 — Powers of 2
# Label: alg:powers2
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Determines whether a positive integer is a power of 2.
#
# Usage: python A9_Powers2.py 1 6 9 8 17

import sys

def power2(n):
    try:
        if n != int(n) or n < 1:
            print(n, 'is an invalid input')
            return None
        else:
            n = int(n)
    except:
        print(n, 'is an invalid input')
        return None
    else:
        x = n
        while x > 1:
            if x % 2 == 0:
                x = int(x / 2)
            else:
                print(n, 'IS NOT a power of 2.')
                return False
        print(n, 'IS a power of 2.')
        return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                power2(int(arg))
            except:
                print(arg, 'is an invalid input.')
    else:
        print('A9_Powers2.py expected at least one additional input.')
