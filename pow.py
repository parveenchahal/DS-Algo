def pow(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    
    if n % 2 != 0:
        t = pow(x, (n - 1) / 2)
        return x * t * t
    else:
        t = pow(x, n / 2)
        return t * t

print(pow(2, 18))