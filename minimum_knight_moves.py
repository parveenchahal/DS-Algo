# https://leetcode.com/problems/minimum-knight-moves/


class Solution:
    
    DIRS = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2))
    
    def _bfs_next_level(self, q, visited, target):
        if len(q) <= 0:
            return False
        for _ in range(len(q)):
            ui, uj = q.popleft()
            for dir in self.DIRS:
                v = (ui + dir[0], uj + dir[1])
                if v in target:
                    return True
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return False
    
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        q1 = deque([(0, 0)])
        q2 = deque([(x, y)])
        visited1 = set([(0, 0)])
        visited2 = set([(x, y)])
        
        steps1 = 0
        steps2 = 0
        
        while len(q1) > 0 and len(q2) > 0:
            steps1 += 1
            if self._bfs_next_level(q1, visited1, visited2):
                return steps1 + steps2
            steps2 += 1
            if self._bfs_next_level(q2, visited2, visited1):
                return steps1 + steps2
        raise
