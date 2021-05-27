# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

def ways_to_split(nums):
    MOD = 1000000007
    n = len(nums)
    if not any(nums):
        pre = 1
        cur = 1
        for i in range(4, n + 1):
            cur = i - 2 + pre
            pre = cur
        return cur % MOD
    sum_so_far = [nums[0]]
    for i in range(1, n):
        sum_so_far.append(sum_so_far[i - 1] + nums[i])
    total = sum_so_far[n - 1]
    one_third = total // 3
    result = 0
    mid_min = 1
    mid_max = n - 2
    while mid_min < n and sum_so_far[0] > sum_so_far[mid_min] - sum_so_far[0]:
        mid_min += 1
    while mid_max > 0 and total - sum_so_far[mid_max] < sum_so_far[mid_max] - sum_so_far[0]:
        mid_max -= 1
    result += max(0, mid_max - mid_min + 1)
    for i in range(1, n):
        if sum_so_far[i] > one_third:
            break
        while mid_min < n and sum_so_far[i] > sum_so_far[mid_min] - sum_so_far[i]:
            mid_min += 1
        mid_max += 15
        mid_max = min(n - 1, mid_max)
        while mid_max < n and total - sum_so_far[mid_max] > sum_so_far[mid_max] - sum_so_far[i]:
            mid_max += 1
        while mid_max > 0 and total - sum_so_far[mid_max] < sum_so_far[mid_max] - sum_so_far[i]:
            mid_max -= 1
        result += mid_max - mid_min + 1
    return result % MOD

r = ways_to_split([7,2,5,5,6,2,10,9])
assert r == 6

r = ways_to_split([1,2,2,2,5,0])
assert r == 3

r = ways_to_split([1,1,1])
assert r == 1

r = ways_to_split([3,2,1])
assert r == 0
