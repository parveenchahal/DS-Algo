#
# https://www.interviewbit.com/problems/maximum-absolute-difference/
#

def max_diff(A):
    m = -0xfffffffffffffffffffffffffff
    j1 = 0
    j2 = 0
    for i in range(1, len(A)):
        xi = A[i] + i
        xj = A[j1] + j1
        m = max(m, xi - xj)
        if xi < xj:
            j1 = i

        xi = i - A[i]
        xj = j2 - A[j2]
        m = max(m, xi - xj)
        if xi < xj:
            j2 = i
    return m

r = max_diff([-39, -24, 82, 95, 91, -65, 16, -76, -56, 70])
assert r == 175
