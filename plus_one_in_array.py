def trim_from_left(A: list):
    for i in range(len(A)):
        if A[0] != 0:
            return A
        A.remove(0)
    return []

def plusOne(A):
    if len(A) == 0:
        return []

    A = trim_from_left(A)
    n = len(A)

    if n <= 0:
        return [1]

    x = A[n - 1] + 1
    A[n - 1] = x % 10
    c = int(x / 10)
    for i in reversed(range(n - 1)):
        x = A[i] + c
        A[i] = x % 10
        c = int(x / 10)
    
    r = []
    if c != 0:
        r.append(c)
    r.extend(A)
    return r

print(plusOne([ 9, 9, 9, 9, 9 ]))