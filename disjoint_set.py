from typing import Union, Any, List

class DisjointSet():

    _map: dict

    def __init__(self):
        self._map = {}

    def add_set(self, v: Union[Any, List]):
        if isinstance(v, list):
            for x in v:
                self._map[x] = v[0]
        else:
            self._map[v] = v

    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        self._map[_b] = _a

    def find(self, v):
        try:
            self._map[v]
        except KeyError:
            return None
        t = v
        while(self._map[t] != t):
            t = self._map[t]

        # Compression
        self._map[v] = t
        
        return t

    def __str__(self):
        return str(self._map)

    def __repr__(self):
        return self.__str__()