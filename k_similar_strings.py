# https://leetcode.com/problems/k-similar-strings/


class Solution:
    
    def _get_conn(self, u, target):
        n = len(u)
        first_unmatched = 0
        for c1,c2 in zip(u, target):
            if c1 != c2:
                break
            first_unmatched += 1
        if first_unmatched >= n:
            return []
        res = []
        for i in range(first_unmatched + 1, n):
            c1 = u[i]
            c2 = target[i]
            if c1 != c2 and target[first_unmatched] == u[i]:
                new_str = u[:first_unmatched] + u[i] + u[first_unmatched + 1: i] + u[first_unmatched] + u[i + 1:]
                res.append(new_str)
        return res
    
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        q = deque([(s1, 0)])
        visited = set(s1)
        while len(q) > 0:
            u, d = q.popleft()
            for v in self._get_conn(u, s2):
                if v == s2:
                    return d + 1
                if v not in visited:
                    visited.add(v)
                    q.append((v, d + 1))
        return -1
