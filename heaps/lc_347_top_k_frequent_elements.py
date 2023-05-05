# https://leetcode.com/problems/top-k-frequent-elements/description/
"""
Solution 1: Using maxheap
Runtime 97 ms Beats 90.81%
Memory 21 MB Beats 9.81%
TC: O(n)+ k*O(logN) - O(n) for Counter
                    - O(n) for heapify
                    - k*logN for heappop operation up to k times
SC: O(n)
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-freq, num) for num, freq in Counter(nums).items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]