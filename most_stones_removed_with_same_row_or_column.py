# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    
    def _dfs(self, u, gr, gc, visited):
        visited.add(u)
        for v in gr[u[0]].union(gc[u[1]]):
            if v not in visited:
                self._dfs(v, gr, gc, visited)
    
    def removeStones(self, stones: List[List[int]]) -> int:
        gr = {}
        gc = {}
        for stone in stones:
            stone = tuple(stone)
            i, j = stone
            try:
                gr[i].add(stone)
            except KeyError:
                gr[i] = set([stone])
            try:
                gc[j].add(stone)
            except KeyError:
                gc[j] = set([stone])
        
        visited = set()
        count = 0
        for stone in stones:
            stone = tuple(stone)
            if stone not in visited:
                self._dfs(stone, gr, gc, visited)
                count += 1
        return len(stones) - count
