# https://leetcode.com/problems/range-sum-query-mutable/

# Method 1 (Using BIT)
class BITForRangeSum:
    def __init__(self, input):
        self._input = list(input)
        self._tree = [0] + list(input)
        n = len(self._tree)
        for i in range(1, n):
            parent = i + (i & -i)
            if parent < n:
                self._tree[parent] += self._tree[i]

    def _prefix_query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self._tree[index]
            index -= (index & -index)
        return res

    def query(self, from_index, to_index):
        return self._prefix_query(to_index) - self._prefix_query(from_index - 1)

    def update(self, index, val):
        diff = val - self._input[index]
        self._input[index] = val
        n = len(self._tree)
        index += 1
        while index < n:
            self._tree[index] += diff
            index += index & -index


class NumArray:

    def __init__(self, nums: List[int]):
        self._bit = BITForRangeSum(nums)
        
    def update(self, index: int, val: int) -> None:
        self._bit.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self._bit.query(left, right)



# Method 2 (Using Segment Tree)
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
            return r1 + r2
        
    def query(self, i, j):
        return self._query(0, i, j, 0, self._n - 1)

class NumArray:

    def __init__(self, nums: List[int]):
        self._seg_tree = SegmentTree(nums, lambda left,right: left + right)
        #print(self._seg_tree._tree)
        
    def update(self, index: int, val: int) -> None:
        self._seg_tree.update(index, val)
        #print(self._seg_tree._tree)
        

    def sumRange(self, left: int, right: int) -> int:
        return self._seg_tree.query(left, right)
