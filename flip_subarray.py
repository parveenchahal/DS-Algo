#
#https://www.interviewbit.com/problems/flip/
#
def flip(A):
    
    n = len(A)
    A = [1 if i == '1' else -1 for i in A]
    if len(list(filter(lambda x: x == -1, A))) == 0:
        return []
    for i in range(1, n):
        A[i] += A[i - 1]
    t = [0]
    t.extend(A)
    A = t

    ma_i = 0
    l = r = 0
    min_diff = 0xffffffffffffffffffffffffffff
    for i in range(1, n + 1):
        if A[i] - A[ma_i] < min_diff:
            min_diff = A[i] - A[ma_i]
            l = ma_i
            r = i
        if A[i] > A[ma_i]:
            ma_i = i
    return (l + 1, r)

r = flip('010')
print(r)