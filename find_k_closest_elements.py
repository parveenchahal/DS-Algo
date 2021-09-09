# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        i = 0
        j = n - k - 1
        lb = 0
        while i <= j:
            mid = (i + j) // 2
            if x - arr[mid] > arr[mid + k] - x:
                i = mid + 1
            else:
                j = mid - 1
        lb = i
        return arr[lb:lb + k]
