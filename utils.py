def parse_int_list(s: str, sep: str = ' ') -> list:
    return [int(x) for x in s.split(sep)]

def parse_float_list(s: str, sep: str = ' ') -> list:
    return [int(x) for x in s.split(sep)]

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
        r.extend([set(x) for x in combinations(arr, i)])
    return r