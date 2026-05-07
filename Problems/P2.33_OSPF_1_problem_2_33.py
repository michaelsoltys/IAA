# Problem 2.33, Page 46 — OSPF
# Label: exr:ospf
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# OSPF routing table simulator using Dijkstra's algorithm.
# Interactive CLI for managing routers, networks, and connections.

import sys

infinity = float('inf')
V = []  # list of vertices
E = {}  # dictionary of directed edges and their costs

def expand(prefix, ranges):
    '''Expands the vertices (given by prefix) into the routers given in the range.'''

    if prefix != 'nt' and prefix != 'rt':
        raise ValueError('expecting rt or nt;', prefix, 'given.')

    for i in ranges.split(','):
        if '-' in i:
            try:
                start, end = i.split('-')
                for k in range(int(start), int(end) + 1):
                    yield prefix + str(k)
            except ValueError:
                print('warning: malformed range', i)
        else:
            try:
                yield prefix + str(int(i))
            except ValueError:
                print('warning: invalid integer', i)

def add(prefix, ranges):
    '''Add routers or networks to the routing table.'''

    for vertex in expand(prefix, ranges):
        if vertex in V:
            print("warning:", vertex, "already added.")
        else:
            V.append(vertex)

def rm(prefix, ranges):
    '''Remove routers or networks from the routing table.'''

    for vertex in expand(prefix, ranges):
        if vertex in V:
            V.remove(vertex)
            connections = []
            for v1, v2 in E:
                if v1 == vertex or v2 == vertex:
                    connections.append((v1, v2))
            for edge in connections:
                del E[edge]
        else:
            print("warning:", vertex, "does not exist.")

def con(src, dest, cost):
    '''Connect src to dest with the given cost.'''

    if src not in V:
        raise KeyError(src + ' is not a known node')
    if dest not in V:
        raise KeyError(dest + ' is not a known node')
    if src == dest:
        raise ValueError('Unable to connect a node to itself.')
    if src.startswith('nt') and dest.startswith('nt'):
        raise ValueError('Unable to connect two networks.')

    cost = int(cost)
    if cost < 0:
        raise ValueError('cannot connect with a negative cost')

    E[(src, dest)] = cost

def find_first_by(distance, candidates):
    '''Finds the candidate with smallest distance.'''

    least_distance = infinity
    best_candidate = None

    for candidate in candidates:
        if distance[candidate] < least_distance:
            least_distance = distance[candidate]
            best_candidate = candidate

    return best_candidate

def neighbours(u, Q):
    '''Returns the neighbouring nodes connected to u.'''

    v = []
    for node in Q:
        if node != u and (u, node) in E:
            v.append(node)
    return v

def tree(source):
    '''Compute tree of shortest paths from source using Dijkstra.'''

    if source.startswith('nt'):
        raise ValueError('Tree source must be a router.')

    distance = {}
    previous = {}

    for v in V:
        distance[v] = infinity
        previous[v] = None

    distance[source] = 0
    Q = list(V)

    while Q:
        u = find_first_by(distance, Q)
        if not u:
            break

        Q.remove(u)

        for v in Q:
            if (u, v) in E:
                alt = distance[u] + E[(u, v)]
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u

    for vertex in V:
        if vertex != source:
            if distance[vertex] < infinity:
                path = []
                print(distance[vertex], '\t : ', end='')
                node = vertex
                path.append(node)
                node = previous[node]
                while node:
                    path.append(node)
                    node = previous[node]
                print(','.join(reversed(path)))
            else:
                print(' ', '\t : ', 'no path to', vertex)

def display():
    '''Display the routing table (link-state database).'''

    print()
    print()
    print('    **          **FROM**    ')
    print('    TO')
    print('    **', end='')
    for src in V:
        print('%6s ' % (src,), end='')
    print()

    for dest in V:
        print('%6s ' % (dest,), end='')
        for src in V:
            if (src, dest) in E:
                print('%6d ' % (E[(src, dest)],), end='')
            else:
                print('       ', end='')
        print()

def quit_program():
    '''Exit the program.'''
    exit()


def main():
    '''Routing table management daemon.'''

    while True:
        try:
            line = input('routed 1.0> ')
            line = line.split()

            command = line[0]
            args = line[1:]

            try:
                if command == 'add':
                    add(*args)
                elif command == 'del':
                    rm(*args)
                elif command == 'con':
                    con(*args)
                elif command == 'display':
                    display(*args)
                elif command == 'quit':
                    quit_program(*args)
                elif command == 'tree':
                    tree(*args)
                else:
                    raise ValueError('Unknown command: ' + command)
            except Exception as e:
                print('error: ', e)
        except (IndexError, EOFError) as e:
            if isinstance(e, EOFError):
                break
            print('error: Enter a command,', e)

if __name__ == '__main__':
    main()
