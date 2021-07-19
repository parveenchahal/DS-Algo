# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    
    def _clone_graph(self, node, visited, cloned_map):
        if node.val in visited:
            return
        visited.add(node.val)
        
        for x in node.neighbors:
            if x.val not in cloned_map:
                cloned_map[x.val] = Node(x.val, [])
            
            # Added Edge for cloned nodes
            cloned_map[node.val].neighbors.append(cloned_map[x.val])
            
            self._clone_graph(x, visited, cloned_map)
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        
        visited = set()
        cloned_map = {}
        
        cloned_map[node.val] = Node(node.val, [])
        self._clone_graph(node, visited, cloned_map)
        
        return cloned_map[node.val]
