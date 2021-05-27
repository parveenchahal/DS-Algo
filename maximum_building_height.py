# https://leetcode.com/problems/maximum-building-height/

from typing import List
import copy

def max_height_between_two(l, r):
    j = r[0]
    i = l[0]
    v = l[1]
    if l[1] < r[1]:
        f = r[1] - l[1]
        i += f
        v = f + l[1]
    elif l[1] > r[1]:
        f = l[1] - r[1]
        j -= f
        v = f + r[1]
    return ((j - i) // 2) + v
        

def normalize(restrictions):
    for i in range(1, len(restrictions)):
        if restrictions[i - 1][1] < restrictions[i][1]:
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]))
    for i in range(len(restrictions) - 2, -1, -1):
        if restrictions[i][1] > restrictions[i + 1][1]:
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]))


def max_building(n: int, restrictions: List[List[int]]) -> int:
    restrictions.insert(0, [1, 0])
    if restrictions[-1][0] < n:
        restrictions.append([n, (n - restrictions[-1][0]) + restrictions[-1][1]])
    restrictions = sorted(restrictions, key=lambda x: x[0])
    normalize(restrictions)
    m = 0
    for i in range(1, len(restrictions)):
        l = restrictions[i - 1]
        r = restrictions[i]
        x = max_height_between_two(l, r)
        m = max(m, x)
    return m

r = max_building(10, [[5,3],[2,5],[7,4],[10,3]])
assert r == 5

r = max_building(10, [[8,5],[9,0],[6,2],[4,0],[3,2],[10,0],[5,3],[7,3],[2,4]])
assert r == 2

r = max_building(5, [[2,1], [4,1]])
assert r == 2

r = max_building(6, [])
assert r == 5