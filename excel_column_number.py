# https://www.interviewbit.com/problems/excel-column-number/
# https://www.interviewbit.com/problems/excel-column-title/

class Solution:
    def titleToNumber(self, s):
        ABC = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('A') + 26)}
        n = len(s)
        result = 0
        for i in range(0, n):
            result *= 26
            result += ABC[s[i]]
        return result

def excel_column_string(n):
    ABC = {i: chr(64 + i) for i in range(1, 26)}
    ABC[0] = 'Z'
    result = ""
    while n > 0:
        r = n % 26
        n = (n // 26)
        if r == 0:
            n -= 1
        result = ABC[r] + result
    return result

x = "JKDGDSFGFNNNJ"

assert x == excel_column_string(excel_column_number(x))
