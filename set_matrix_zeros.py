def set_zeroes(mat):
    n = len(mat)
    m = len(mat[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in zero_rows:
        for j in range(m):
            mat[i][j] = 0
    
    for j in zero_cols:
        for i in range(n):
            mat[i][j] = 0
    return mat

mat = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1]
]

mat = set_zeroes(mat)
print(mat)