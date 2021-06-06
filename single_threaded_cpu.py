# https://leetcode.com/problems/single-threaded-cpu/

from typing import List
import heapq
class Node:
    def __init__(self, i, e, p):
        self.i = i
        self.e = e
        self.p = p
    
    def __lt__(self, o):
        if self.p == o.p:
            return self.i < o.i
        return self.p < o.p

class Solution:

    def add_until(self, h, tasks, i, t):
        n = len(tasks)
        while i < n and tasks[i].e <= t:
            heapq.heappush(h, tasks[i])
            i += 1
        return i

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i] = Node(i, tasks[i][0], tasks[i][1])
        tasks.sort(key=lambda x: x.e)
        h = []
        i = self.add_until(h, tasks, 0, tasks[0].e)
        heapq.heapify(h)
        t = tasks[0].e
        result = []
        while True:
            cur = heapq.heappop(h)
            result.append(cur.i)
            t += cur.p
            i = self.add_until(h, tasks, i, t)
            if i < n and len(h) <= 0:
                t = tasks[i].e
                i = self.add_until(h, tasks, i, tasks[i].e)
            if len(h) <= 0:
                break
        return result

r = Solution().getOrder([[100,100],[1000000000,1000000000]])
assert r == [0,1]

r = Solution().getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]])
assert r == [5,0,1,3,2,4]

r = Solution().getOrder([[1,2],[2,4],[3,2],[4,1]])
assert r == [0,2,3,1]

r = Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])
assert r == [4,3,2,0,1]