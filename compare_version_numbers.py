# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_arr = list(map(int, version1.split('.')))
        v2_arr = list(map(int, version2.split('.')))
        n1 = len(v1_arr)
        n2 = len(v2_arr)
        if n2 > n1:
            v1_arr.extend([0] * (n2 - n1))
        elif n1 > n2:
            v2_arr.extend([0] * (n1 - n2))
        if v1_arr < v2_arr:
            return -1
        if v1_arr > v2_arr:
            return 1
        return 0
