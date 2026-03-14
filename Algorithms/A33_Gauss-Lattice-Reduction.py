# Algorithm 33, Page 163 — Gauss Lattice Reduction (2D)
# Label: alg:gausslattice
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# 2D Gaussian lattice reduction. Input is a file containing a lattice
# basis as semicolon-separated vectors with comma-separated components.
#
# Usage: python A33_Gauss-Lattice-Reduction.py input_A33_Gauss-Lattice-Reduction.txt

from fractions import Fraction as frac
import sys

def dot(X, Y):
    sum = 0
    for x, y in zip(X, Y):
        sum += x * y
    return sum

def norm(X):
    return dot(X, X)

def reduce(v1, v2):
    v1 = [frac(v) for v in v1]
    v2 = [frac(v) for v in v2]
    while True:
        if norm(v2) < norm(v1):
            v1, v2 = v2, v1
        m = round(dot(v1, v2) / norm(v1), 0)
        if m == 0:
            return ([float(v) for v in v1], [float(v) for v in v2])
        v2 = [u2 - m * u1 for u2, u1 in zip(v2, v1)]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'r')
        v1, v2 = ([eval(x) for x in vector.split(',')]
                   for vector in file.read().replace('\n', '').replace(' ', '').split(';') if vector)
        file.close()
        R = [str(v) for v in reduce(v1, v2)]
        m = max([len(v) for v in R])
        print('  Result from lattice reduction:')
        for v in R:
            print(v.rjust(m + 5))
    else:
        print('A33_Gauss-Lattice-Reduction.py expected 1 additional input.', len(sys.argv) - 1, 'given.')
