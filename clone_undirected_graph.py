# https://www.interviewbit.com/problems/clone-graph/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self._cloneGraph(node, None, set(), {})


    def _cloneGraph(self, node, new_node, visited, new_node_map):
        if node is None:
            return
        visited.add(node)
        if new_node is None:
            new_node = UndirectedGraphNode(node.label)
            new_node_map[new_node.label] = new_node

        for n in node.neighbors:
            if n not in visited:
                n_t = UndirectedGraphNode(n.label)
                new_node_map[n_t.label] = n_t
                self._cloneGraph(n, n_t, visited, new_node_map)
            new_node_map[node.label].neighbors.append(new_node_map[n.label])
        return new_node

n703 = UndirectedGraphNode(703)
n43 = UndirectedGraphNode(43)
n279 = UndirectedGraphNode(279)

n703.neighbors.append(n279)
n703.neighbors.append(n703)
n703.neighbors.append(n43)

n279.neighbors.append(n703)
n279.neighbors.append(n43)


n43.neighbors.append(n279)
n43.neighbors.append(n43)
n43.neighbors.append(n703)


new_node = Solution().cloneGraph(n703)
print(new_node)