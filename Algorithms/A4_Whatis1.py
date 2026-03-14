# Algorithm 4, Page 9 — What Is It? (1)
# Label: alg:whatis1
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Computes product using binary representation.
#
# Usage: python A4_Whatis1.py <m> <n>

import sys

def alg(m, n):
    x = m
    y = n
    z = 0
    i = 0
    while x != 0:
        print('Iteration ' + str(i).rjust(3) + ' : x = ' + str(x) + ', y = ' + str(y) + ',',
              'and z = ' + str(z))
        if x % 2 == 1:
            z += y
        x = x // 2
        y *= 2
        i += 1
    print('\nInput: m =', m, 'and n =', n,
          '\nOutput: z =', z)
    return z

if __name__ == '__main__':
    if len(sys.argv) == 3:
        m = sys.argv[1]
        n = sys.argv[2]
        try:
            m = int(m)
            n = int(n)
        except:
            print('Invalid inputs for A4_Whatis1.py')
        else:
            alg(m, n)
    else:
        print('A4_Whatis1.py expected 2 additional arguments.', len(sys.argv) - 1, 'given.')
