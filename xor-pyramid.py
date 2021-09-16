# https://codeforces.com/contest/983/problem/B


class Node:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.max = val
        self.left = left
        self.right = right
 
lookup = None
def prepare_lookup(arr, n):
    global lookup
    lookup = [[0] * n for _ in range(n)]
    t = [None] * n
    for i, x in enumerate(arr):
        t[i] = Node(x, i, i)
        lookup[i][i] = x
    while len(t) > 1:
        nt = []
        for i in range(len(t) - 1):
            l = t[i].left
            r = t[i + 1].right
            x = Node(t[i].val ^ t[i + 1].val, l, r)
            x.max = max(x.max, t[i].max, t[i + 1].max)
            lookup[l][r] = x.max
            nt.append(x)
        t = nt
 
def solve(q_list):
    for q in q_list:
        l, r = q
        print(lookup[l - 1][r - 1])
 
n = int(input())
arr = list(map(int, input().split(' ')))
prepare_lookup(arr, n)
ql = int(input())
q = []
for _ in range(ql):
    q.append(list(map(int, input().split(' '))))
solve(q)
