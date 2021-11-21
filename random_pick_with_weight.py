# https://leetcode.com/problems/random-pick-with-weight/


class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.w = w
        for i in range(1, n):
            self.w[i] += self.w[i - 1]
        self.total_sum = self.w[-1]

    def pickIndex(self) -> int:
        w = self.w
        left = 0
        right = len(w) - 1
        num = random.randint(1, self.total_sum)
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            if num <= w[mid]:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
