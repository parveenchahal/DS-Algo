# https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

import heapq

class Solution(object):
    
    def _dijkstra(self, master, i, j):
        heap = [[0, i, j]]
        while len(heap) > 0:
            node = heapq.heappop(heap)
            dist = node[0]
            node_i = node[1]
            node_j = node[2]
            if self._visited[node_i][node_j]:
                continue
            
            if node_i == self._target[0] and node_j == self._target[1]:
                return dist
            
            self._visited[node_i][node_j] = True
            
            if self._links[node_i][node_j] is None:
                continue
            for x in self._links[node_i][node_j]:
                x_i = x[0]
                x_j = x[1]
                x_d = x[2]
                if not self._visited[x_i][x_j]:
                    heapq.heappush(heap, [dist + x_d, x_i, x_j])
            
            
    def findShortestPath(self, master) -> int:
        NM = 200
        START = 50
        self._visited = [[False] * NM for _ in range(NM)]
        self._links = [[None] * NM for _ in range(NM)]
        self._target = None
        self._populate_graph(master, START, START)
        if self._target is None:
            return -1
        return self._dijkstra(master, START, START)

    
    def _populate_graph(self, master, i, j):
        if master.isTarget():
            self._target = [i, j]
        if self._links[i][j] is not None:
            return
        self._links[i][j] = []
        if master.canMove('L'):
            d = master.move('L')
            self._links[i][j].append([i - 1, j, d])
            self._populate_graph(master, i - 1, j)
            d = master.move('R')
            self._links[i - 1][j].append([i, j, d])
        
        if master.canMove('R'):
            d = master.move('R')
            self._links[i][j].append([i + 1, j, d])
            self._populate_graph(master, i + 1, j)
            d = master.move('L')
            self._links[i + 1][j].append([i, j, d])
            
        if master.canMove('U'):
            d = master.move('U')
            self._links[i][j].append([i, j - 1, d])
            self._populate_graph(master, i, j - 1)
            d = master.move('D')
            self._links[i][j - 1].append([i, j, d])
            
        if master.canMove('D'):
            d = master.move('D')
            self._links[i][j].append([i, j + 1, d])
            self._populate_graph(master, i, j + 1)
            d = master.move('U')
            self._links[i][j + 1].append([i, j, d])