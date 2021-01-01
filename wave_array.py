# https://www.interviewbit.com/problems/wave-array/

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def wave(arr):
    arr = sorted(arr)
    n = len(arr)
    for i in range(1, n, 2):
        if arr[i - 1] < arr[i]:
            swap(arr, i - 1, i)
        if i + 1 < n and arr[i + 1] < arr[i]:
            swap(arr, i + 1, i)
    return arr


r = wave([54,53,56,7,2,547])
assert r == [7, 2, 54, 53, 547, 56]

r = wave([1])
assert r == [1]

r = wave([1, 2, 0])
assert r == [1, 0, 2]

r = wave([ 5, 1, 3, 2, 4 ])
assert r == [2, 1, 4, 3, 5 ]