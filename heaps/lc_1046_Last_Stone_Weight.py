# https://leetcode.com/problems/last-stone-weight/description/
"""
Solution 1: Using max heap
Runtime 31 ms Beats 96.76%
Memory 16.3 MB Beats 31.64%
TC:O(n logn)
SC:O(n)
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:return stones[0]
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while maxheap and len(maxheap) >= 2:
            y, x = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
            if x==y:continue
            heapq.heappush(maxheap, -(y-x))
        return -maxheap[0] if len(maxheap)==1 else 0