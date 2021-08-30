class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = [set() for _ in range(n)]
        for road in roads:
            a, b = road
            edges[a].add(b)
            edges[b].add(a)
        
        max_rank = -1
        for i in range(n):
            for j in range(i + 1, n):
                cur = len(edges[i]) + len(edges[j])
                if i in edges[j]:
                    cur -= 1
                max_rank = max(max_rank, cur)
        return max_rank
