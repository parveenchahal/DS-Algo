# https://www.interviewbit.com/problems/power-of-two-integers/

from math import sqrt

def is_power(n):
    if n == 1:
        return 1
    i = 2
    j = int(sqrt(n))
    for k in range(i, j + 1):
        t = 0
        while True:
            x = pow(k, t)
            if x > n:
                break
            if x == n:
                return 1
            t += 1
    return 0

assert 1 == is_power(1)
assert 0 == is_power(2)
