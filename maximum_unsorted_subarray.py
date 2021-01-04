# https://www.interviewbit.com/problems/maximum-unsorted-subarray/

def unsorted_subarray(arr):
    n = len(arr)
    min_from_right = [arr[n - 1]]
    for i in range(n - 2, -1, -1):
        pre = n - 2 - i
        if arr[i] < min_from_right[pre]:
            min_from_right.append(arr[i])
        else:
            min_from_right.append(min_from_right[pre])
    min_from_right = list(reversed(min_from_right))
    max_from_left = [arr[0]]
    for i in range(1, n):
        if(arr[i] > max_from_left[i - 1]):
            max_from_left.append(arr[i])
        else:
            max_from_left.append(max_from_left[i - 1])
    l = -1
    r = -1
    for i in range(0, n):
        if max_from_left[i] != min_from_right[i]:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if max_from_left[i] != min_from_right[i]:
            r = i
            break
    return [l, r] if l != -1 and r != -1 else [-1]
    



r = unsorted_subarray([1,3,2,4,5])
assert r == [1,2]

r = unsorted_subarray([1,2,3,4,5])
assert r == [-1]