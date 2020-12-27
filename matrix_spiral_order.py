def matrix_spiral_order(A):
    r_min = 0
    r_max = len(A) - 1
    c_min = 0
    c_max = len(A[0]) - 1
    result = []
    while(r_min <= r_max and c_min <= c_max):
        
        i = r_min
        j = c_min
        while(j <= c_max):
            result.append(A[i][j])
            j += 1
        
        i += 1
        j = c_max
        while(i <= r_max):
            result.append(A[i][j])
            i += 1

        i = r_max
        j -= 1
        while(j >= c_min and r_min != r_max and c_min != c_max):
            result.append(A[i][j])
            j -= 1

        i -= 1
        j = c_min
        while(i > r_min and r_min != r_max and c_min != c_max):
            result.append(A[i][j])
            i -= 1

        r_min += 1
        r_max -= 1

        c_min += 1
        c_max -= 1

    return result


mat = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
r = matrix_spiral_order(mat)

print(r)
