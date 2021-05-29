import math

# babylonianSquareRoot
def square_root(n):
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('num should be greater than equal to zero')
    x = n
    y = 1
    while(x - y > 0.00001):
        x = (x + y) / 2
        y = n / x
    return x


def _______square_root(n):
    if n == 0:
        return 0
    if n < 0:
        raise ValueError('num should be greater than equal to zero')
    s = pow(2, math.log2(n) * 0.5)
    return round(s, 5)