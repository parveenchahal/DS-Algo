class DisjointSet():

    _map: dict
    _rank: dict

    def __init__(self):
        self._map = {}
        self._rank = {}
        
    def make_set(self, x):
        self._map[x] = x
        self._rank[x] = 0

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return
        if self._rank[a] == self._rank[b]:
            self._map[b] = a
            self._rank[a] += 1
            del self._rank[b]
        elif self._rank[a] > self._rank[b]:
            self._map[b] = a
            del self._rank[b]
        else:
            self._map[a] = b
            del self._rank[a]

    def find(self, x):
        try:
            self._map[x]
        except KeyError:
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
