def substrCount(n, s):
    dp = [[]] * n
    for i in range(n):
        dp[i] = [False] * n

    count = 0

    for i in range(0, n):
        dp[i][i] = True
        count += 1

    for size in range(2, n + 1):
        for i in range(0, n - size + 1):
            l = i
            r = i + size - 1
            if s[l] == s[r]:
                _l = l + 1
                _r = r - 1
                if(_l > _r or dp[_l][_r]):
                    dp[l][r] = True
                    count += 1
    return count


if __name__ == '__main__':
    s = "abcbaba"
    result = substrCount(len(s), s)
    print(result)
