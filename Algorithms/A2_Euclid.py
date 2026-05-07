# Algorithm 2, Page 6 — Euclid's Algorithm
# Label: alg:euclid
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Computes the greatest common factor of two natural numbers.
#
# Usage: python A2_Euclid.py <a> <b>

import sys

def euclid(a, b):
    if a <= 0 or b <= 0 or a != int(a) or b != int(b):
        raise ValueError("Invalid inputs for Euclid's.")
    m = int(a)
    n = int(b)
    r = m % n
    while r > 0:
        m = n
        n = r
        r = m % n
    print('The GCF of', a, 'and', b, 'is', str(n) + '.')
    return n

if __name__ == '__main__':
    if len(sys.argv) > 3:
        raise TypeError('Too many inputs for Euclids GCF.')
    elif len(sys.argv) < 3:
        raise TypeError('Too few inputs for Euclids GCF.')
    else:
        euclid(int(sys.argv[1]), int(sys.argv[2]))
