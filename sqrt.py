import math

def sqrt(num):
    if num == 0:
        return 0
    if num < 0:
        raise ValueError('num should be greater than equal to zero')
    s = pow(2, math.log2(num) * 0.5)
    return round(s, 5)

if __name__ == '__main__':
    r = sqrt(81)
    print(r)