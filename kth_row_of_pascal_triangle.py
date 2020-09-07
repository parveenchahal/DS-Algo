def get_row(k):
    p = 1
    result = [p,]
    for i in range(1, k + 1):
        c = p * (k - i + 1) / i
        result.append(int(c))
        p = c
    return result

if __name__ == '__main__':
    r = get_row(100)
    print(r)