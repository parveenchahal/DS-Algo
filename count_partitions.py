#
# https://www.interviewbit.com/problems/partitions
#


# @param A : integer
# @param B : list of integers
# @return an integer
def count_partition(A, B):
    s = sum(B)
    if s % 3 != 0:
        return 0

    # If all elements are zero.
    if len(list(filter(lambda x: x != 0, B))) == 0:
        return int(((A - 2) * (A - 1)) / 2)

    t = int(s / 3)
    c = 0
    def count(a, k):
        nonlocal t
        nonlocal c
        if k <= 0:
            c += 1
            return
        s = 0
        for i in range(0, len(a)):
            s += a[i]
            if s == t:
                count(a[i + 1:], k - 1)
    count(B, 3)
    return c


l = [0] * 9
r = count_partition(len(l), l)
assert r == 28

l = [1] * 9
r = count_partition(len(l), l)
assert r == 1

l = [1, 2, 3, 0, 3]
r = count_partition(len(l), l)
assert r == 2

l = [0, 1, -1, 0]
r = count_partition(len(l), l)
assert r == 1
