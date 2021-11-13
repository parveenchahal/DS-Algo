# https://leetcode.com/problems/reconstruct-itinerary/


class Solution:
    
    def _make_graph(self, tickets):
        graph = defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
        for _,v in graph.items():
            v.sort()
        return graph
    
    def _find_itinerary(self, u, graph, tickets_count, res):
        for v in graph[u]:
            edge = (u, v)
            if tickets_count[edge] > 0:
                tickets_count[edge] -= 1
                self._find_itinerary(v, graph, tickets_count, res)
        res.append(u)
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = self._make_graph(tickets)
        tickets_count = Counter(map(tuple, tickets))
        res = []
        self._find_itinerary('JFK', graph, tickets_count, res)
        return res[::-1]
