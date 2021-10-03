# https://leetcode.com/problems/add-strings/

# Method 1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        carry = 0
        res = []
        while i1 >= 0 or i2 >= 0 or carry > 0:
            x1 = ord(num1[i1]) - ord('0') if i1 >= 0 else 0
            x2 = ord(num2[i2]) - ord('0') if i2 >= 0 else 0
            s = x1 + x2 + carry
            res.append(str(s % 10))
            carry = s // 10
            i1 -= 1
            i2 -= 1
        return ''.join(res[::-1])


# Method 2
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return num2
        if num2 == '0':
            return num1
        if len(num1) == 1 and len(num2) == 1:
            x1 = ord(num1) - ord('0')
            x2 = ord(num2) - ord('0')
            return str(x1 + x2)
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = list(num1)
        num2 = list(num2)
        
        result = num1
        j = -1
        for i in range(len(num2) - 1, -1, -1):
            a = result[j]
            b = num2[i]
            result[j] = self.addStrings(a, b)
            j -= 1
        
        c = '0'
        for i in range(len(result) - 1, -1, -1):
            result[i] = self.addStrings(c, result[i])
            c = result[i][:-1] if len(result[i]) > 1 else '0'
            result[i] = result[i][-1]
        s = ''.join(result)
        if c != '0':
            s = c + s
        return s
