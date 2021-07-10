# https://leetcode.com/problems/integer-to-roman/

# Method 1
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10])


# Method 2
class Solution:
    def _get_values(self, x):
        if x == 0:
            return ''
        
        m = [
            {1: 'I', 5: 'V'},
            {1: 'X', 5: 'L'},
            {1: 'C', 5: 'D'},
            {1: 'M'}
        ]
        
        n_zeros = 0
        t = x
        while True:
            t //= 10
            if t == 0:
                break
            n_zeros += 1
        
        f = int(str(x)[0])
        if f == 1:
            return m[n_zeros][1]
        if f > 1 and f <= 3:
            return m[n_zeros][1] * f
        if f == 4:
            return m[n_zeros][1] + m[n_zeros][5]
        if f == 5:
            return m[n_zeros][5]
        if f > 5 and f < 9:
            return m[n_zeros][5] + (m[n_zeros][1] * (f - 5))
        if f == 9:
            return m[n_zeros][1] + m[n_zeros + 1][1]
    
    def intToRoman(self, num: int) -> str:
        result = ''
        i = 1
        while True:
            x = int(num % (10 ** i))
            result = self._get_values(x) + result
            num -= x
            if num <= 0:
                break
            i += 1
        return result
