#
# https://www.interviewbit.com/problems/min-sum-path-in-matrix/
#

def min_sum_path(A):
    n = len(A)
    m = len(A[0])
    dp = [[]] * n
    for i in range(n):
        dp[i] = [0xfffffffffffffffff] * m

    dp[0][0] = A[0][0]
    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + A[i + 1][j])
            if j + 1 < m:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + A[i][j + 1])
    return dp[n - 1][m - 1]

r = min_sum_path([
        [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
    ])

assert r == 8