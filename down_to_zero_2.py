# https://www.hackerrank.com/challenges/down-to-zero-ii/problem

MAX_VALUE = 10 ** 6
lookup = list(range(MAX_VALUE + 1))
for i in range(2, MAX_VALUE + 1):
    lookup[i] = min(lookup[i], lookup[i - 1] + 1)
    for j in range(2, i + 1):
        k = i * j
        if k > MAX_VALUE:
            break
        lookup[k] = min(lookup[k], lookup[i] + 1)
    

def downToZero(n):
    return lookup[n]


result = downToZero(7273)
assert result == 9
