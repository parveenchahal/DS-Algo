# https://leetcode.com/problems/k-similar-strings/


class Solution:
    
    def _get_conn(self, s, target):
        n = len(s)
        
        # find first unmatch
        first_unmatch = 0
        while s[first_unmatch] == target[first_unmatch]:
            first_unmatch += 1
        
        res = []
        for i in range(n):
            if s[i] != target[i]: 
                if s[i] != target[i] and s[first_unmatch] == target[i]: 
                    new_s = list(s)
                    new_s[first_unmatch], new_s[i] = new_s[i], new_s[first_unmatch]
                    res.append(''.join(new_s))
        return res
    
    
    def _bfs(self, x, target):
        if x == target:
            return 0
        k = 1
        q = deque([x])
        visited = set([x])
        while len(q) > 0:
            for _ in range(len(q)):
                u = q.popleft()
                for v in self._get_conn(u, target):
                    if v == target:
                        return k
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            k += 1
        return k
    
    def kSimilarity(self, s1: str, s2: str) -> int:
        return self._bfs(s1, s2)
