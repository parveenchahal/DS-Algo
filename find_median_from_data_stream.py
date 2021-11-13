# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def addNum(self, num: int) -> None:
        if len(self._min_heap) > 0:
            x = heapq.heappop(self._min_heap)
            heapq.heappush(self._max_heap, -x)
        heapq.heappush(self._max_heap, -num)
        while len(self._max_heap) - len(self._min_heap) > 1:
            x = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, x)

    def findMedian(self) -> float:
        if len(self._max_heap) == len(self._min_heap):
            return (-self._max_heap[0] + self._min_heap[0]) / 2
        return -self._max_heap[0]
       
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
