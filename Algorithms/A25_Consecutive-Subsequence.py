# Algorithm 25, Page 89 — Consecutive Subsequence
# Label: alg:consecutive-2
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Finds the largest consecutive subsequence sum in a sequence of reals.
#
# Usage: python A25_Consecutive-Subsequence.py input_A25_Consecutive-Subsequence.txt
#        python A25_Consecutive-Subsequence.py 1,3,-4.02,3.14159,.86

import sys

def css(R):
    M = [R[0]]
    for j in range(1, len(R)):
        if M[j - 1] > 0:
            M.append(M[j - 1] + R[j])
        else:
            M.append(R[j])
    s = max(M)
    i = M.index(s)
    ss = []
    while R[i] != M[i]:
        ss = [R[i]] + ss
        i -= 1
    ss = [R[i]] + ss
    return (s, ss)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        arg1 = ''.join(sys.argv[1:])
        try:
            file = open(arg1, 'r')
            args = file.read().replace('\n', '')
            file.close()
        except FileNotFoundError:
            args = arg1
        try:
            args = [arg.replace(' ', '') for arg in args.split(',')]
            args = [eval(arg) for arg in args if arg]
            args = [arg for arg in args if arg <= float('inf')]
        except:
            print('A25_Consecutive-Subsequence.py expected a sequence of real numbers, separated by commas.')
        else:
            (s, ss) = css(args)
            print('The largest sum,', str(s) + ',', 'results from subsequence:\n  ', ss)
    else:
        print('A25_Consecutive-Subsequence.py expected an additional input.')
