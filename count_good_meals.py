# https://leetcode.com/problems/count-good-meals/

from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pow_of_two = []
        cur = 1
        pow_of_two.append(cur)
        # Max 2^20 + 2^20 ~= 2 ^ 21
        for _ in range(1, 22):
            cur *= 2
            pow_of_two.append(cur)
            
        # Either count all freq initially and subtract one by one
        # Or Add in dict one by one and increase freq.
        deliciousness_count = {}
        for x in deliciousness:
            try:
                deliciousness_count[x] += 1
            except KeyError:
                deliciousness_count[x] = 1
        
        result = 0
        for x in deliciousness:
            deliciousness_count[x] = max(0, deliciousness_count[x] - 1)
            for p in pow_of_two:
                if p >= x:
                    y = p - x
                    if y in deliciousness_count:
                        c = deliciousness_count[y]
                        result += c
                        result %= 1000000007
        return result
