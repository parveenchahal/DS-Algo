#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
#

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        
        s = sum(arr)
        if s % 3 != 0:
            return 0

        # If all elements are zero.
        if len(list(filter(lambda x: x != 0, arr))) == 0:
            return int(((A - 2) * (n - 1)) / 2)

        t = int(s / 3)
        c = 0
        def count(a, k):
            nonlocal t
            nonlocal c
            if k <= 0:
                c += 1
                return
            s = 0
            for i in range(0, len(a)):
                s += a[i]
                if s == t:
                    count(a[i + 1:], k - 1)
        count(arr, 3)
        return c
