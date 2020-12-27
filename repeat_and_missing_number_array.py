# Problem - https://www.interviewbit.com/problems/repeat-and-missing-number-array

def repeat_and_missing_number(arr):
    n = len(arr)
    s = sum(arr)
    a = s - sum(set(arr))
    diff = (n * (n + 1)) // 2 - s
    b = a + diff
    return a, b

r = repeat_and_missing_number([3, 1, 2, 5, 3])
print(r)
