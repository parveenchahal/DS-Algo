def max_diff(A):
    m = -0xfffffffffffffffffffffffffff
    j = 0
    for i in range(1, len(A)):
        xi = A[i] + i
        xj = A[j] + j
        m = max(m, xi - xj)
        if xi < xj:
            j = i
    j = 0
    for i in range(1, len(A)):
        xi = i - A[i] 
        xj = j - A[j]
        m = max(m, xi - xj)
        if xi < xj:
            j = i
    return m

r = max_diff([-39, -24, 82, 95, 91, -65, 16, -76, -56, 70])
assert r == 175
