# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self._max_heap, -num)
        if len(self._min_heap) > 0 and num > self._min_heap[0]:
            heapq.heappush(self._max_heap, -self._min_heap[0])
            heapq.heappop(self._min_heap)
        
        while len(self._max_heap) - len(self._min_heap) > 1:
            heapq.heappush(self._min_heap, -self._max_heap[0])
            heapq.heappop(self._max_heap)

    def findMedian(self) -> float:
        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]
        elif len(self._max_heap) == len(self._min_heap):
            return (-self._max_heap[0] + self._min_heap[0]) / 2
        else:
            raise
