# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        i = 0
        j = n - 1
        while i < j:
            if knows(i, j):
                i += 1
            else:
                j -= 1
        for k in range(n):
            if k != i and not knows(k, i):
                return -1
        for k in range(n):
            if k != i and knows(i, k):
                return -1
        return i
      
