# Problem 2.6, Page 35 — Kruskal
# Label: exr:kruskal_component
# An Introduction to the Analysis of Algorithms (4th Edition)

from os.path import exists
from sys import stdout
import re
import copy
import os.path
import sys


def MergingComponents(grid, index, D):
    k = D[grid.edges[index].v1 - 1]
    l = D[grid.edges[index].v2 - 1]

    for j in range(len(D)):
        if D[j] == l:
            D[j] = k

def hasNoCycle(r, s, D):
    return D[r] != D[s]

def Kruskal(grid, D):
    insertSort(grid)
    T = Grid(grid.degree, [])
    for i in range(len(grid.edges)):
        if hasNoCycle(grid.edges[i].v1 - 1, grid.edges[i].v2 - 1, D):
            T.addEdge(grid.edges[i])
            MergingComponents(grid, i, D)
        display(T)
    return T

def getGridFromFile(filepath="graph.txt"):
    if not exists(filepath):
        return None
    f = open(filepath, 'r')
    s = f.read()
    f.close()

    if not re.match(r'^\s*\d+\s*:(\s*\(\s*\d+\s*,\s*\d+\s*;\s*\d+\s*\)\s*,?)*$', s):
        return None

    t = s.partition(':')
    degree = int(t[0].strip(), 10)
    s = t[2]

    edges = []

    for e in re.findall(r'\d+\s*,\s*\d+\s*;\s*\d+', s):
        args = []
        for n in re.findall(r'\d+', e):
            args.append(int(n, 10))
        edges.append(Edge(*args))

    return Grid(degree, edges)

class Grid:
    """Represents an n-grid."""

    def __init__(self, degree, edges=None):
        self.degree = degree
        self.edges = edges if edges is not None else []

    def addEdge(self, edge):
        self.edges.append(edge)

    def hasEdge(self, v1, v2):
        for edge in self.edges:
            if (edge.v1 == v1 and edge.v2 == v2) or (edge.v2 == v1 and edge.v1 == v2):
                return True
        return False


class Edge:
    """Represents a weighted graph edge."""

    def __init__(self, v1, v2, cost):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

def isAllowed(vertex, degrees):
    return 0 <= vertex <= degrees * degrees

def isConnected(grid):
    T = []
    Edges = copy.deepcopy(grid.edges)
    T.append(Edges[0].v1)
    T.append(Edges[0].v2)
    Edges.remove(Edges[0])
    t = 0
    while t < len(T):
        u = 0
        while u < len(Edges):
            if len(Edges) > 0 and Edges[u].v1 == T[t]:
                T.append(Edges[u].v2)
                Edges.remove(Edges[u])
            elif 0 < len(Edges) and u < len(Edges) and Edges[u].v2 == T[t]:
                T.append(Edges[u].v1)
                Edges.remove(Edges[u])
            else:
                u = u + 1
        t = t + 1
    T = sorted(T)
    Nodes = []
    for i in range(1, len(T)):
        if T[i] == T[i - 1]:
            pass
        else:
            Nodes.append(T[i - 1])
    if len(Nodes) >= grid.degree:
        return True
    else:
        return False

def isGrid(grid):
    for i in range(0, len(grid.edges)):
        if isAllowed(grid.edges[i].v1, grid.degree) and isAllowed(grid.edges[i].v2, grid.degree):
            if abs(grid.edges[i].v1 - grid.edges[i].v2) == 1:
                pass
            elif abs(grid.edges[i].v1 - grid.edges[i].v2) == grid.degree:
                pass
            else:
                return False
        else:
            return False
    if isConnected(grid):
        return True
    else:
        return False

def insertSort(myGrid):
    for i in range(len(myGrid.edges)):
        for j in range(len(myGrid.edges)):
            if myGrid.edges[i].cost < myGrid.edges[j].cost:
                temp = myGrid.edges[j]
                myGrid.edges[j] = myGrid.edges[i]
                myGrid.edges[i] = temp

def display(graph):
    for i in range(graph.degree):
        if i > 0:
            for j in range(graph.degree):
                if j > 0:
                    stdout.write(' ')
                if graph.hasEdge(graph.degree * (i - 1) + j + 1, graph.degree * i + j + 1):
                    stdout.write('|')
                else:
                    stdout.write(' ')
            print()

        for j in range(graph.degree):
            if j > 0:
                if graph.hasEdge(graph.degree * i + j, graph.degree * i + j + 1):
                    stdout.write('-')
                else:
                    stdout.write(' ')
            stdout.write('*')
        print()

def AuxiliaryArray(n):
    return list(range(n * n))

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "graph.txt"
    if not os.path.exists(filename):
        print("File not found:", filename)
    else:
        grid = getGridFromFile(filename)
        if grid is None:
            print("Invalid file format")
        else:
            display(grid)
            if isGrid(grid):
                D = AuxiliaryArray(grid.degree)
                display(Kruskal(grid, D))
            else:
                print("Not a grid")
