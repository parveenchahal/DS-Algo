# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0
        cur = -0x7ffffffffff
        for x,y in pairs:
            if cur < x:
                res += 1
                cur = y
        return res
