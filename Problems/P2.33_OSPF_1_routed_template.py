# Problem 2.33, Page 46 — OSPF
# Label: exr:ospf
# An Introduction to the Analysis of Algorithms (4th Edition)
#
# Routing table template — a skeleton for the OSPF routing simulator.

import readline  # gives command history to input()

V = []  # list of vertices (routers 'rt' and networks 'nt')
E = {}  # dictionary of edges and their costs


def add_rt(*routers):
    global V
    '''Add routers to the routing table.'''
    for router in routers:
        try:
            V.index(router)
            print(router, "already present")
        except ValueError:
            V.append(router)
    print('add rt', routers)


def del_rt(*routers):
    global V
    '''Delete routers from the routing table.'''
    for router in routers:
        print(router)
        try:
            V.remove(router)
            print('del rt', routers)
        except ValueError as e:
            print(router, 'not in list')


def add_nt(*networks):
    '''Add networks to the routing table.'''
    print('add nt', networks)

def del_nt(*networks):
    '''Delete networks from the routing table.'''
    print('del nt', networks)

def con(x, y, z):
    '''Connect node x and node y with cost z.'''
    print('con', x, y, z)

def display():
    '''Display the routing table (link-state database).'''
    print('display')

def tree(x):
    '''Compute tree of shortest paths from x using Dijkstra.'''
    print('tree', x)

def quit_program():
    '''Exit the daemon.'''
    exit(0)

functions = {
    'add rt': add_rt, 'del rt': del_rt,
    'add nt': add_nt, 'del nt': del_nt,
    'con': con, 'display': display, 'tree': tree, 'quit': quit_program
}

while True:
    line = input('sfwr4C03router 1.0> ')
    line = line.split()
    if not line:
        continue
    nodes = line[1].split(',') if len(line) > 1 else []
    if line[0] == 'add':
        add_rt(nodes)
    elif line[0] == 'del':
        del_rt(nodes)
    elif line[0] == 'quit':
        quit_program()
    else:
        print('unknown command:', line[0])
