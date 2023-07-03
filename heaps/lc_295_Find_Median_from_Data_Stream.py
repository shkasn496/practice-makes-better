# https://leetcode.com/problems/find-median-from-data-stream/description/
"""
Solution 1: Using two heaps to store elements in sorted order. 
            Left boundary heap is a max heap
            right boundary heap is a min heap
Runtime 513 ms Beats 65.42%
Memory 38 MB Beats 85.29%
TC:
    init(): O(1)
    addNum(): O(logN)
    findMedian(): O(1)

SC: O(N)
"""
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.left_maxheap = []
        self.right_minheap= []
        return

    def addNum(self, num: int) -> None:
        heappush(self.left_maxheap, -num)
        heappush(self.right_minheap, -heappop(self.left_maxheap))

        if len(self.left_maxheap) < len(self.right_minheap):
            heappush(self.left_maxheap, -heappop(self.right_minheap))
        return

    def findMedian(self) -> float:
        if len(self.left_maxheap) > len(self.right_minheap):
            return -self.left_maxheap[0]
        else:
            return (self.right_minheap[0] - self.left_maxheap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()