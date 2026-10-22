# Algorithm 10, Page 35 — Kruskal
# Label: alg:kruskal
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Minimum-cost spanning tree. Cycle test is Algorithm 11 (Merging
# components): D[i] is the component of vertex i.
#
# Input: n by n adjacency matrix, comma-separated. 0 means no edge.
# Diagonal must be 0. The graph must be undirected (symmetric).
#
# Usage: python A10_Kruskal.py input_A10_Kruskal.txt

import sys


def merge_components(D, r, s):
    k = D[r]
    l = D[s]
    for j in range(len(D)):
        if D[j] == l:
            D[j] = k


def kruskal(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            c = matrix[i][j]
            if c != 0:
                edges.append((i, j, c))
    edges.sort(key=lambda e: e[2])
    D = list(range(n))
    T = []
    cost = 0
    for r, s, c in edges:
        if D[r] != D[s]:
            T.append((r, s))
            cost += c
            merge_components(D, r, s)
    return T, cost


def read_matrix(path):
    rows = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = []
            for x in line.split(','):
                n = float(x.strip())
                row.append(int(n) if n == int(n) else n)
            rows.append(row)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError('Input must be a square adjacency matrix.')
    for i in range(n):
        if rows[i][i] != 0:
            raise ValueError('Diagonal entries must be 0.')
        for j in range(i + 1, n):
            if rows[i][j] != rows[j][i]:
                raise ValueError('Input graph must be undirected.')
            if rows[i][j] < 0:
                raise ValueError('Edge costs must be nonnegative.')
    return rows


def fmt_cost(c):
    if c == int(c):
        return str(int(c))
    return str(c)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Expected 1 argument, got ' + str(len(sys.argv) - 1) + '.')
    matrix = read_matrix(sys.argv[1])
    T, cost = kruskal(matrix)
    kind = 'MCST' if len(T) == len(matrix) - 1 else 'minimum spanning forest'
    print('The edges', T, 'form a', kind, 'with total cost', fmt_cost(cost) + '.')
