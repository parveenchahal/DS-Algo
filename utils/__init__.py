from ._disjoint_set import DisjointSet
from ._graph import Edge, Graph
from ._heaps import BinaryHeap
from ._square_root import square_root

MOD = int(f'1{("0" * 8)}7')

def cmp_to_key(cmp):
    '''Can be used as key for sorted function
       This function also present in functools'''
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
            
        def __lt__(self, o):
            return cmp(self.obj, o.obj) < 0
    return K

def parse_int_list(s: str, sep: str = ' ') -> list:
    return map(int, s.split(sep))

def parse_float_list(s: str, sep: str = ' ') -> list:
    return map(float, s.split(sep))

def print_matrix(mat):
    for r in mat:
        for x in r:
            print(f'{x}\t', end='')
        print()

def combinations(arr: list, r: int) -> list:
    from copy import deepcopy
    n = len(arr)
    result = []
    def wrapper(buf: list, i, k):
        buf.append(arr[i])
        k -= 1
        if k <= 0:
            result.append(buf)
            return
        for j in range(i + 1, n - k + 1):
            wrapper(deepcopy(buf), j, k)
    for i in range(n - r + 1):
        wrapper([], i, r)
    return result


def power_set(arr: list) -> list:
    n = len(arr)
    r = [set()]
    for i in range(1, n + 1): 
        r.extend(map(set, combinations(arr, i)))
    return r

def radix_sort(nums):
    n = len(nums)
    max_num = str(max(nums))
    max_len = len(max_num)

    for i in range(n):
        nums[i] = str(nums[i])[::-1]
        d = max_len - len(nums[i])
        if d > 0:
            nums[i] = nums[i] + ('0' * d)

    for k in range(max_len):
        bucket = [[] for _ in range(10)]
        for i in range(n):
            bucket[int(nums[i][k])].append(nums[i])
        c = 0
        for b in range(10):
            for x in bucket[b]:
                nums[c] = x
                c += 1
    for i in range(n):
        nums[i] = int(nums[i][::-1])

def pow(x: float, n: int):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x * x
    if n == -1:
        return 1 / x
    if n == -2:
        return (1 / x) * (1 / x)
    
    if n & 1 == 1:
        m = pow(x, n // 2)
        return x * m * m
    else:
        m = pow(x, n // 2)
        return m * m
