# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List

def min_subarray(nums: List[int], p: int) -> int:
    n = len(nums)
    s = sum(nums)
    r = s % p
    if r == 0:
        return 0
    sum_so_far = 0
    m = {0: -1}
    MAX = n
    result = MAX
    for i in range(n):
        sum_so_far += nums[i]
        x = sum_so_far % p - r
        if x < 0:
            x += p
        if x in m:
            result = min(result, i - m[x])
        m[sum_so_far % p] = i
    return result if result != MAX else -1

r = min_subarray([3,1,4,2], 6)
assert r == 1

r = min_subarray([6,3,5,2], 9)
assert r == 2