
class SegmentTree:
    def __init__(self, arr, merger):
        self._n = len(arr)
        self._merger = merger
        self._tree = [None] * (4 * self._n)
        self._build(arr, 0, 0, self._n - 1)
        
    def _build(self, arr, tree_index, left, right):
        if left == right:
            self._tree[tree_index] = arr[left]
            return
        mid = left + (right - left) // 2
        left_tree_index = 2 * tree_index + 1
        right_tree_index = 2 * tree_index + 2
        self._build(arr, left_tree_index, left, mid)
        self._build(arr, right_tree_index, mid + 1, right)
        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])
        
    def _update(self, target_index, val, tree_index, left, right):
        if left == right:
            self._tree[tree_index] = val
            return
        left_tree_index = 2 * tree_index + 1
        right_tree_index = 2 * tree_index + 2
        mid = left + (right - left) // 2
        if target_index >= left and target_index <= mid:
            self._update(target_index, val, left_tree_index, left, mid)
        else:
            self._update(target_index, val, right_tree_index, mid + 1, right)
        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])
        
    def update(self, index, val):
        self._update(index, val, 0, 0, self._n - 1)
        
    def _query(self, tree_index, i, j, left, right):
        if i == left and j == right:
            return self._tree[tree_index]
        mid = left + (right - left) // 2
        if i >= left and j <= mid:
            return self._query(2 * tree_index + 1, i, j, left, mid)
        elif i >= mid + 1 and j <= right:
            return self._query(2 * tree_index + 2, i, j, mid + 1, right)
        else:
            r1 = self._query(2 * tree_index + 1, i, mid, left, mid)
            r2 = self._query(2 * tree_index + 2, mid + 1, j, mid + 1, right)
            return self._merger(r1, r2)
        
    def query(self, i, j):
        return self._query(0, i, j, 0, self._n - 1)
