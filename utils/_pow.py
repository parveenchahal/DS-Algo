def pow(x: float, n: int):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1 / x

    if n & 1 == 1:
        m = self.pow(x, n // 2)
        return x * m * m
    else:
        m = self.pow(x, n // 2)
        return m * m
