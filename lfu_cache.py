# https://leetcode.com/problems/lfu-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.left = self.right = None
        
class DLL:
    def __init__(self):
        self._head = Node('HEAD', 'HEAD')
        self._last = Node('LAST', 'LAST')
        self._head.right, self._last.left = self._last, self._head
    
    def is_empty(self):
        return self._head.right == self._last
    
    def remove(node):
        left, right = node.left, node.right
        left.right = right
        right.left = left
    
    def remove_last(self):
        if not self.is_empty():
            last_node = self._last.left
            DLL.remove(last_node)
            return last_node
        return None
            
    def add_first(self, node):
        left = self._head
        right = self._head.right
        left.right, node.left = node, left
        node.right, right.left = right, node

class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._min_freq = 1
        self._freq_map = defaultdict(DLL)
        self._node_map = {}
        
    def get(self, key: int) -> int:
        try:
            node = self._node_map[key]
            DLL.remove(node)
            if self._freq_map[node.freq].is_empty():
                del self._freq_map[node.freq]
                if node.freq == self._min_freq:
                    self._min_freq += 1
        except KeyError:
            return -1
        node.freq += 1
        self._freq_map[node.freq].add_first(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity <= 0:
            return
        if self.get(key) != -1:
            self._node_map[key].val = value
            return
        if self._size >= self._capacity:
            self._remove_lfu()
        node = Node(key, value)
        self._node_map[key] = node
        self._size += 1
        self._freq_map[1].add_first(node)    
        self._min_freq = min(self._min_freq, 1)
    
    def _remove_lfu(self):
        min_freq = self._min_freq
        lfu_node = self._freq_map[min_freq].remove_last()
        del self._node_map[lfu_node.key]
        self._size -= 1
        self._min_freq = 1
