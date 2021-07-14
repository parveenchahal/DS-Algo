# https://leetcode.com/problems/multiply-strings/

class Solution:
    def _sum(self, num1, num2):
        if len(num1) > len(num2):
            num2, num1 = num1, num2
        min_len = min(len(num1), len(num2))
        res = []
        c = 0
        i = 0
        while i < min_len:
            x = num1[i] + num2[i]
            x += c
            res.append(x % 10)
            c = x // 10
            i += 1
        for j in range(i, len(num2)):
            x = num2[j]
            x += c
            res.append(x % 10)
            c = x // 10
        if c > 0:
            res.append(c)
        return res
    
    def multiply(self, num1: str, num2: str) -> str:
        num1 = list(map(int, reversed(num1)))
        num2 = list(map(int, reversed(num2)))
        if len(num1) > len(num2):
            num2, num1 = num1, num2
        n1 = len(num1)
        n2 = len(num2)
        res = []
        c = 0
        for i in range(n1):
            t = [0] * i
            c = 0
            for j in range(n2):
                m = num1[i] * num2[j]
                m += c
                if j < n2 - 1:
                    t.append(m % 10)
                    c = m // 10
                else:
                    t.append(m)
            res = self._sum(res, t)
        res = ''.join(map(str, reversed(res))).lstrip('0')
        return res if len(res) > 0 else '0'
