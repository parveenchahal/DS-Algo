class BinaryHeap():
    _values: list
    _size: int

    def __init__(self, values: list=[], cmp=None):
        if cmp is None:
            def default_cmp(x, y):
                if x.__eq__(y):
                    return 0
                if x.__lt__(y):
                    return -1
                return 1
            self._cmp = default_cmp
        else:
            self._cmp = cmp
        if not isinstance(values, list):
            raise TypeError('values is not type of list')
        from copy import deepcopy
        self._values = deepcopy(values)
        self._size = len(values)
        self._heapify()


    def insert(self, value):
        self._values.append(value)
        self._size += 1
        index = self._sift_up(self._size - 1, value)
        self._values[index] = value

    def poll(self):
        v = self._values[0]
        l = self._values.pop()
        self._size -= 1
        if self._size <= 0:
            return v
        index = self._sift_down(0, l)
        self._values[index] = l
        return v

    def size(self):
        return self._size

    def _heapify(self):
        for i in range(BinaryHeap._parent_index(self._size - 1), -1, -1):
            v = self._values[i]
            index = self._sift_down(i, v)
            self._values[index] = v

    def _sift_up(self, index, v):
        while index > 0:
            parent_index = BinaryHeap._parent_index(index)
            if self._cmp(v, self._values[parent_index]) >= 0:
                break
            self._values[index] = self._values[parent_index]
            index = parent_index
        return index

    def _sift_down(self, index, v):
        last_index = self._size - 1
        last_parent = BinaryHeap._parent_index(last_index)

        while index <= last_parent:
            lci = BinaryHeap._left_child_index(index)
            rci = BinaryHeap._right_child_index(index)

            smaller_child_index = lci

            if rci <= last_index and self._cmp(self._values[lci], self._values[rci]) > 0:
                smaller_child_index = rci
            
            if self._cmp(v, self._values[smaller_child_index]) <= 0:
                break

            self._values[index] = self._values[smaller_child_index]
            index = smaller_child_index

        return index

    @staticmethod
    def _parent_index(index):
        return (index - 1) >> 1

    @staticmethod
    def _left_child_index(index):
        return (index << 1) + 1

    @staticmethod
    def _right_child_index(index):
        return (index << 1) + 2

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return self.__str__()
