from utils import *
from io import StringIO
from copy import deepcopy
from sys import maxsize
import json

class Node():
    parent: int
    dist: int

    def __init__(self, parent, dist, p_id):
        self.parent = parent
        self.dist = dist
        self.p_id = p_id

    def __str__(self):
        return str(self.__dict__)

def _generate_id(v, via_set):
    if len(via_set) > 0:
        via_set = str(via_set)
    else:
        via_set = '{}'
    return f'[{v}, {via_set}]'

def _find_min_path_with_via_set(v, via_set, dist_map, mat):
    if len(via_set) > 0 and v not in via_set:
        parent = -1
        p_id = None
        min_dist = maxsize
        for p in via_set:
            t_s = deepcopy(via_set)
            t_s.remove(p)
            id = _generate_id(p, t_s)
            t = mat[p][v] + dist_map[id].dist
            if t < min_dist:
                parent = p
                p_id = id
                min_dist = t
        dist_map[_generate_id(v, via_set)] = Node(parent, min_dist, p_id)

def find_path(mat, start):
    n = len(mat)

    locations = []
    for i in range(0, n):
        if i != start:
            locations.append(i)

    # Find sets of all locations except staring point which is zero.
    sets = power_set(locations)

    dist_map = {}

    # Creating entries in dist_map from start to all locations via empty set.
    for loc in locations:
        id = _generate_id(loc, set())
        dist_map[id] = Node(start, mat[start][loc], _generate_id(start, {}))


    for s in sets:
        for loc in locations:
            _find_min_path_with_via_set(loc, s, dist_map, mat)

    # Going back to start via all locations.
    _find_min_path_with_via_set(start, set(locations), dist_map, mat)

    # Tracing path in reverse order.
    path = [start]
    p_id = _generate_id(start, set(locations))

    while(dist_map.get(p_id, None)):
        node: Node = dist_map[p_id]
        path.append(node.parent)
        p_id = node.p_id
    
    return list(reversed(path))


#================== Inputs ======================

f = StringIO(
'''4 4
0 1 15 6
2 0 7 3
9 6 0 12
10 4 8 0
22''')

n, m = parse_int_list(f.readline())

mat = []

for i in range(n):
    mat.append(parse_int_list(f.readline()))

s = int(f.readline())

path = find_path(mat, s)

print(' -> '.join([str(x) for x in path]))

