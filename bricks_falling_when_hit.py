# https://leetcode.com/problems/bricks-falling-when-hit/


class Solution:
    
    DIRS = ((-1, 0), (0, 1), (0, -1), (1, 0))
    
    def _is_stable(self, ds, roof_node, x):
        return ds.find(roof_node) == ds.find(x)
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        
        hits = list(map(lambda x: x + [grid[x[0]][x[1]]], hits))
        
        for hit in hits:
            if grid[hit[0]][hit[1]] == 1:
                grid[hit[0]][hit[1]] = 0
        
        ds = DisjointSet()
        roof_node = (-1, -1)
        ds.make_set(roof_node)
        
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                ds.make_set((i, j))
        
        for j in range(C):
            if grid[0][j] == 1:
                ds.union(roof_node, (0, j))
        
        for i in range(R):
            for j in range(C):
                x = grid[i][j]
                if x == 1:
                    for dir in self.DIRS:
                        vi, vj = i + dir[0], j + dir[1]
                        if vi < 0 or vi >= R or vj < 0 or vj >= C or grid[vi][vj] == 0:
                            continue
                        ds.union((vi, vj), (i, j))
        
        res = []
        for i in range(len(hits) - 1, -1, -1):
            hi, hj, x = hits[i]
            if x == 0:
                res.append(0)
                continue
            hit = (hi, hj)
            grid[hi][hj] = 1
            ds.make_set(hit)
            if hi == 0:
                ds.union(hit, roof_node)
            count = 0
            for dir in self.DIRS:
                vi, vj = hi + dir[0], hj + dir[1]
                v = (vi, vj)
                if vi < 0 or vi >= R or vj < 0 or vj >= C or grid[vi][vj] == 0:
                    continue
                if not self._is_stable(ds, roof_node, (vi, vj)) and ds.find(hit) != ds.find(v):
                    count += ds.size_of(v)
                ds.union(hit, v)
            
            if self._is_stable(ds, roof_node, hit):
                res.append(count)
            else:
                res.append(0)
        res.reverse()
        return res

class DisjointSet():

    _map: dict
    _rank: dict
    _size: dict

    def __init__(self):
        self._map = {}
        self._rank = {}
        self._size = {}
        
    def make_set(self, x):
        self._map[x] = x
        self._rank[x] = 0
        self._size[x] = 1

    def size_of(self, x):
        p = self.find(x)
        if p is not None:
            return self._size[p]
        return 0

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return
        if self._rank[a] == self._rank[b]:
            self._map[b] = a
            self._rank[a] += 1
            self._size[a] += self._size[b]
            del self._rank[b]
            del self._size[b]
        elif self._rank[a] > self._rank[b]:
            self._map[b] = a
            self._size[a] += self._size[b]
            del self._rank[b]
            del self._size[b]
        else:
            self._map[a] = b
            self._size[b] += self._size[a]
            del self._rank[a]
            del self._size[a]

    def find(self, x):
        if x not in self._map:
            return None
        p = x
        while self._map[p] != p:
            p = self._map[p]
        # Compression
        self._map[x] = p
        return p
    
    def distinct_set_count(self):
        count = 0
        for k,v in self._map.items():
            if k == v:
                count += 1
        return count

    def __str__(self):
        return str(self._map)

    def __repr__(self):
        return self.__str__()
