# https://www.interviewbit.com/problems/gas-station/
# https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        available_fuel = 0
        start = 0
        less = 0
        for i in range(n):
            available_fuel += gas[i] - cost[i]
            if available_fuel < 0:
                less += available_fuel
                available_fuel = 0
                start = i + 1
        return start if (available_fuel + less) >= 0 else -1

r = Solution().canCompleteCircuit([ 2, 3, 4 ], [ 3, 4, 3 ])
assert r == -1

r = Solution().canCompleteCircuit([4], [5])
assert r == -1

r = Solution().canCompleteCircuit([1,2], [2,1])
assert r == 1

r = Solution().canCompleteCircuit([1,1,2,3,2,2,1], [1,2,1,4,1,2,1])
assert r == 2