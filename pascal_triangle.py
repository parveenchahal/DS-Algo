# https://www.interviewbit.com/problems/pascal-triangle/

def pascal_triangle(n):
    result = []
    if n <= 0:
        return result
    result.append([1,])
    if n == 1:
        return result
    result.append([1, 1,])
    if n == 2:
        return result
    for k in range(2, n):
        t = [1,]
        for i in range(1, k):
            t.append(result[k - 1][i - 1] + result[k - 1][i])
        t.append(1)
        result.append(t)
    return result
r = pascal_triangle(0)
print(r)
r = pascal_triangle(1)
print(r)
r = pascal_triangle(2)
print(r)
r = pascal_triangle(3)
print(r)
r = pascal_triangle(4)
print(r)
r = pascal_triangle(5)
print(r)