# Algorithm 27, Page 125 — Perfect Matching
# Label: alg:pm
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Randomized algorithm to detect perfect matchings in graphs.
# Mode "any": any perfect matching. Mode "fl": first-half/last-half matching.
#
# Usage: python A27_Perfect-Matching.py input_A27_Perfect-Matching.txt any 100

import numpy as np
from numpy.linalg import det
from copy import deepcopy as copy
from math import sqrt
import sys

def pm(A, mode, iter_count=100):
    if mode == 'any':
        s = pre_any(A)
        if s:
            A, I, J, m = s
        else:
            return -1
    elif mode == 'fl':
        s = pre_first_last(A)
        if s:
            A, I, J, m = s
        else:
            return -1
    else:
        print('Invalid mode')
        return -1

    M = 2 * m + 1
    c = 0
    while c < iter_count:
        if post(A, I, J, m, M):
            return True
        c += 1
    return False

def pre_any(A):
    A = copy(A)
    si, sj = A.shape
    if si != sj:
        print('Non-square input matrix')
        return False
    if si % 2 != 0:
        print('Uneven number of vertices')
        return False
    I = []
    J = []
    m = 0
    for i in range(si):
        if A[i][i] != 0:
            A[i][i] = 0
        for j in range(sj):
            if A[i][j] != 0:
                I.append(i)
                J.append(j)
                m += 1
    if m < 1:
        return False
    return (A, I, J, m)

def pre_first_last(A):
    A = copy(A)
    si, sj = A.shape
    if si != sj:
        print('Non-square input matrix')
        return False
    if si % 2 != 0:
        print('Uneven number of vertices')
        return False
    I = []
    J = []
    m = 0
    for i in range(int(si / 2)):
        for j in range(int(sj / 2), sj):
            if A[i][j] != 0:
                I.append(i)
                J.append(j)
                m += 1
        for j in range(int(sj / 2)):
            if A[i][j] != 0:
                A[i][j] = 0
    for i in range(int(si / 2), si):
        for j in range(int(sj / 2), sj):
            if A[i][j] != 0:
                A[i][j] = 0
        for j in range(int(sj / 2)):
            if A[i][j] != 0:
                I.append(i)
                J.append(j)
                m += 1
    if m < 1:
        return False
    return (A, I, J, m)

def post(A, I, J, m, M):
    new = np.random.randint(1, M, m)
    i = 0
    while i < m:
        A[I[i]][J[i]] = new[i]
        i += 1
    if det(A) != 0:
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('A27_Perfect-Matching.py expected 2-3 inputs.', len(sys.argv) - 1, 'given')
    else:
        try:
            file = open(sys.argv[1], 'r')
            A = [a for a in file.read().replace('\n', ',').replace(' ', '').split(',') if a]
            file.close()
            A = [int(a) for a in A]
        except FileNotFoundError:
            print('Couldn\'t find file', sys.argv[1])
        except ValueError:
            print('Non-integer values in file', sys.argv[1])
        else:
            l = sqrt(len(A))
            if l != int(l):
                print('Input is not an adjacency matrix - invalid number of entries')
            else:
                l = int(l)
                A = np.array([A[i:i + l] for i in range(0, l * l, l)])
                mode = sys.argv[2]
                if len(sys.argv) > 3:
                    iter_count = int(sys.argv[3])
                else:
                    iter_count = 100
                result = pm(A, mode, iter_count)
                if result == -1:
                    pass
                elif result:
                    print('A perfect matching exists')
                else:
                    print('Most likely, no perfect matching exists')
