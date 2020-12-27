# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def minimum_swaps(arr):
    n = len(arr)
    count = 0
    i = 0
    while i < n:
        x = arr[i] - 1
        if x != i:
            swap(arr, x, i)
            count += 1
            continue
        i += 1
    return count

arr = [2, 3, 4, 1, 5]
r = minimum_swaps(arr)
assert r == 3

arr = [1, 3, 5, 2, 4, 6, 7]
r = minimum_swaps(arr)
assert r == 3