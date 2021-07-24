# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f'[{self.key},{self.val}]'


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('Should be greater than 0')
        self._capacity = capacity
        self._head = None
        self._end = None
        self._map = {}
    
    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        node = self._map[key]
        if node == self._head:
            return node.val
        self._delete(node)
        self._insert(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        node = None
        if key in self._map:
            node = self._map[key]
            node.val = value
            self._delete(node)
            self._insert(node)
            return
        if len(self._map) >= self._capacity:
            self._delete_last()
        node = Node(key, value)
        self._map[key] = node
        self._insert(node)
    
    def _insert(self, node):
        if self._head is None:
            node.left = node.right = None
            self._head = self._end = node
            return
        node.left = None
        self._head.left = node
        node.right = self._head
        self._head = node
        
    def _delete(self, node):
        pre = node.left
        nex = node.right
        if pre is None and nex is None:
            self._head = self._end = None
            return
        if pre is None:
            self._head = nex
            self._head.left = None
            return
        if nex is None:
            self._end = pre
            self._end.right = None
            return
        pre.right = nex
        nex.left = pre
    
    def _delete_last(self):
        node = self._end
        del self._map[node.key]
        self._delete(node)
