#
# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
#

def solve(A, B):
    d = 0
    for i in range(1, len(A)):
        a = abs(A[i - 1] - A[i])
        b = abs(B[i - 1] - B[i])
        d += max(a, b)
    return d

if __name__ == '__main__':
    r = solve([0, 1, 1], [0, 1, 2])
    print(r)
    