# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    
    def _is_bipartite(self, graph, u, color, visited):
        if u in visited:
            #print(visited[u] == color)
            return True if visited[u] == color else False
        visited[u] = color
        found = True
        for v in graph[u]:
            found = found and self._is_bipartite(graph, v, not color, visited)
        return found
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        found = True
        for u in range(len(graph)):
            if u not in visited:
                found = found and self._is_bipartite(graph, u, True, visited)
        return found
