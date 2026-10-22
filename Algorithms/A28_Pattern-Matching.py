# Algorithm 28, Page 129 — Pattern Matching
# Label: alg:pattern
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Binary pattern matching using matrix products.
# Uses Rabin-Miller from A29_Rabin-Miller.py for prime generation.
#
# Usage: python A28_Pattern-Matching.py 1011001 00101001110110101100101010

import numpy as np
import sys
import importlib.util

# Import Rabin-Miller from sibling file
_spec = importlib.util.spec_from_file_location(
    "rabin_miller",
    __file__.replace("A28_Pattern-Matching.py", "A29_Rabin-Miller.py")
)
rabin_miller = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rabin_miller)

Ma = dict()
Ma['0'] = np.array([[1, 0], [1, 1]])
Ma['1'] = np.array([[1, 1], [0, 1]])
Mainv = dict()
Mainv['0'] = np.array([[1, 0], [-1, 1]])
Mainv['1'] = np.array([[1, -1], [0, 1]])

def pattern_matching(x, y):
    n = len(x)
    m = len(y)
    mm = n * m * m + 1
    p = 4
    while not rabin_miller.RabinMiller(p):
        p = np.random.randint(2, mm)
    A = M(x)
    B = M(y[:n])
    i = 0
    while n + i < m:
        if np.array_equal(A, B):
            if x == y[i:n + i]:
                return (True, i)
        B = np.dot(np.dot(Mainv[y[i]], B), Ma[y[n + i]])
        i += 1
    if np.array_equal(A, B):
        if x == y[-n:]:
            return (True, i)
    return False

def M(s):
    result = np.array([[1, 0], [0, 1]])
    i = 0
    while i < len(s):
        result = np.dot(result, Ma[s[i]])
        i += 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 3:
        result = pattern_matching(sys.argv[1], sys.argv[2])
        if result:
            print('Matching substring found starting at index ' + str(result[1]) + '.')
        else:
            print('No matching substring found.')
    else:
        print('A28_Pattern-Matching.py expected 2 binary string inputs.', len(sys.argv) - 1, 'args given.')
