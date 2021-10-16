class DisjointSet():

    _map: dict
    _rank: dict

    def __init__(self):
        self._map = {}
        self._rank = {}
        self._size = {}
        
    def make_set(self, x):
        self._map[x] = x
        self._rank[x] = 0
        self._size[x] = 1

    def size_of(self, x):
        p = self.find(x)
        if p is not None:
            return self._size[p]
        return 0

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return
        if self._rank[a] == self._rank[b]:
            self._map[b] = a
            self._rank[a] += 1
            self._size[a] += self._size[b]
            del self._rank[b]
            del self._size[b]
        elif self._rank[a] > self._rank[b]:
            self._map[b] = a
            self._size[a] += self._size[b]
            del self._rank[b]
            del self._size[b]
        else:
            self._map[a] = b
            self._size[b] += self._size[a]
            del self._rank[a]
            del self._size[a]

    def find(self, x):
        if x not in self._map:
            return None
        p = x
        while self._map[p] != p:
            p = self._map[p]
        # Compression
        self._map[x] = p
        return p
    
    def distinct_set_count(self):
        count = 0
        for k,v in self._map.items():
            if k == v:
                count += 1
        return count

    def __str__(self):
        return str(self._map)

    def __repr__(self):
        return self.__str__()
