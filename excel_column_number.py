# https://www.interviewbit.com/problems/excel-column-number/
class Solution:
    def titleToNumber(self, s):
        ABC = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('A') + 26)}
        n = len(s)
        result = 0
        for i in range(0, n):
            result *= 26
            result += ABC[s[i]]
        return result


# https://www.interviewbit.com/problems/excel-column-title/
class Solution:
    def convertToTitle(self, n):
        ABC = {i + 1: chr(ord('A') + i) for i in range(0, 26)}
        result = ""
        while n > 0:
            r = n % 26
            n = (n // 26)
            if r == 0:
                result = 'Z' + result
                n -= 1
            else:
                result = ABC[r] + result
        return result
