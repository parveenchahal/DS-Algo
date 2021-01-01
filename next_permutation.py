# https://www.interviewbit.com/problems/next-permutation/

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def reverse(arr, i, j):
    while(i < j):
        swap(arr, i, j)
        i += 1
        j -= 1

def next_permutation(arr):
    n = len(arr)
    if n < 2:
        return arr
    prev = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if arr[i] < prev:
            j = n - 1
            while(j > i):
                if arr[j] > arr[i]:
                    break
                j -= 1
            swap(arr, i, j)
            reverse(arr, i + 1, n - 1)
            return arr
        prev = arr[i]
    return list(reversed(arr))

r = next_permutation([1, 2, 3, 1])
assert r == [1, 3, 1, 2]

r = next_permutation([1])
assert r == [1]

r = next_permutation([1, 2, 3])
assert r == [1, 3, 2]

r = next_permutation([3, 2, 1])
assert r == [1, 2, 3]
