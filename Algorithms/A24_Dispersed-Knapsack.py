# Algorithm 24, Page 83 — Dispersed Knapsack
# Label: alg:dispknap
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Greedy solution to the dispersed knapsack problem.
#
# Input: comma-separated list of positive integers; first is capacity C,
# rest are weights.
#
# Usage: python A24_Dispersed-Knapsack.py input_A24_Dispersed-Knapsack.txt
#        python A24_Dispersed-Knapsack.py 17,1,2,4,8,16

import sys

def dks(C, W):
    if C != int(C) or C <= 0:
        print('Capacity must be a positive integer.')
        return None
    for w in W:
        if w != int(w) or w <= 0:
            print('Weights must be positive integers.')
            return None
    W = list(W)
    W.sort(reverse=True)
    S = []
    s = 0
    for i in range(len(W)):
        if s + W[i] <= C:
            S.append(i)
            s += W[i]
    S = [W[i] for i in S]
    return (s, S)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        arg1 = ''.join(sys.argv[1:])
        try:
            file = open(arg1, 'r')
            args = file.read().replace('\n', '').replace(' ', '').split(',')
            file.close()
        except FileNotFoundError:
            args = arg1.split(',')
        args = [arg for arg in args if arg]
        try:
            args = [int(arg) for arg in args]
        except ValueError:
            print('Capacity and weights must be integers.')
        else:
            if len(args) > 1:
                if all([arg > 0 for arg in args]):
                    C = args[0]
                    W = args[1:]
                    (s, S) = dks(C, W)
                    print('The maximum weight,', str(s) + ',',
                          'can be reached with weights:\n  ', S)
                else:
                    print('Capacity and weights must be positive.')
            else:
                print('No weights given.')
    else:
        print('A24_Dispersed-Knapsack.py expected at least 1 additional input.')
