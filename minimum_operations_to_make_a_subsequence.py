# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

def binary_search(ls, x):
    n = len(ls)
    l = 0
    r = len(ls) - 1
    while l <= r:
        mid = (l + r) // 2
        if mid + 1 < n and ls[mid + 1] < x:
            l = mid + 1
        elif ls[mid] >= x:
            r = mid - 1
        else:
            return mid
    return -1

def lis(arr):
    n = len(arr)
    ls = [arr[0]]
    for i in range(1, n):
        ind = binary_search(ls, arr[i])
        if ind < 0:
            ls[0] = arr[i]
        elif ind + 1 < len(ls):
            ls[ind + 1] = arr[i]
        else:
            ls.append(arr[i])
    return len(ls)


def min_operations(target, arr):
    m = len(target)
    index_map = {x: i for i, x in enumerate(target)}
    index_arr = []
    for x in arr:
        try:
            index_arr.append(index_map[x])
        except KeyError:
            pass
    return m - (lis(index_arr) if len(index_arr) > 0 else 0)


r = min_operations([5,1,3], [9,4,2,3,4])
assert r == 2

r = min_operations([6,4,8,1,3,2], [4,7,6,2,3,8,6,1])
assert r == 3

r = min_operations([1,3,8], [2,6])
assert r == 3