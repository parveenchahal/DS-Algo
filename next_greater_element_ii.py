# https://leetcode.com/problems/next-greater-element-ii/


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n2 = n * 2
        st = []
        res = [-1] * n
        for k in range(n2 - 1, -1, -1):
            i = k % n
            x = nums[i]
            while len(st) > 0 and x >= st[-1]:
                st.pop()
            if i < n:
                if len(st) > 0:
                    res[i] = st[-1]
                else:
                    res[i] = -1
            st.append(x)
        return res
