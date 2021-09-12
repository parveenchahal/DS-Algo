# https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        ans = 0
        while left <= right:
            mid = (left + right) >> 1
            mis = arr[mid] - 1 - mid
            if mis < k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        mis = arr[ans] - 1 - ans
        if k <= mis:
            return k
        return arr[ans] + k - mis
