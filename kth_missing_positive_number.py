# https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        ans = None
        while left <= right:
            mid = (left + right) >> 1
            missing = arr[mid] - mid - 1
            if missing < k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans is None:
            return k
        missing = arr[ans] - ans - 1
        return arr[ans] + k - missing
