# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    n_to_s = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred',
        1000: 'Thousand',
        1000000: 'Million',
        1000000000: 'Billion'
    }
        
    def _numberToWords(self, num: int) -> str:
        if num <= 0:
            return []
        
        if num >= 1 and num <= 19:
            return [self.n_to_s[num]]
                
        ten = 10
        hundred = 100
        thousand = 1000
        million = 1000000
        billion = 1000000000
        
        res = []
        
        n = num // billion
        if n > 0:
            res.extend(self._numberToWords(n))
            res.append(self.n_to_s[billion])
            num -= billion * n
        
        n = num // million
        if n > 0:
            res.extend(self._numberToWords(n))
            res.append(self.n_to_s[million])
            num -= million * n
            
        n = num // thousand
        if n > 0:
            res.extend(self._numberToWords(n))
            res.append(self.n_to_s[thousand])
            num -= thousand * n
            
        n = num // hundred
        if n > 0:
            res.extend(self._numberToWords(n))
            res.append(self.n_to_s[hundred])
            num -= hundred * n
        
        if num >= 20 and num <= 99:
            n = num // 10
            t = n * 10
            res.append(self.n_to_s[t])
            num -= t
            res.extend(self._numberToWords(num))
        else:
            res.extend(self._numberToWords(num))
        
        return res
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        return ' '.join(self._numberToWords(num))
