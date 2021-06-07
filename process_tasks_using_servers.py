# https://leetcode.com/problems/process-tasks-using-servers/

import heapq
from typing import List


class Server:
    def __init__(self, i, w):
        self.i = i
        self.w = w
        
    def __lt__(self, o):
        if self.w != o.w:
            return self.w < o.w
        return self.i < o.i

class Allocation:
    def __init__(self, server, end_time):
        self.server = server
        self.end_time = end_time
    def __lt__(self, o):
        return self.end_time < o.end_time


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(tasks)
        
        result = [None] * n
        
        allocation = []
        free_servers = [Server(i, servers[i]) for i in range(len(servers))]
        heapq.heapify(free_servers)
                
        t = 0
        i = 0
        while i < n:
            while len(allocation) > 0:
                if allocation[0].end_time > t:
                    break
                a = heapq.heappop(allocation)
                heapq.heappush(free_servers, a.server)
            if len(free_servers) <= 0:
                t = allocation[0].end_time
                continue
            while i < n and i <= t and len(free_servers) > 0:
                s = heapq.heappop(free_servers)
                result[i] = s.i
                heapq.heappush(allocation, Allocation(s, t + tasks[i]))
                i += 1
            t += 1
        return result
