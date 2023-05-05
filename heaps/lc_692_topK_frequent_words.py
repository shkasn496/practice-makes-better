# https://leetcode.com/problems/top-k-frequent-words/description/
"""
Solution 1: Using maxheap
Runtime 63 ms Beats 30.70%
Memory 16.5 MB Beats 7.47%
TC: O(n)+ k*O(logN) - O(n) for Counter
                    - O(n) for heapify
                    - k*logN for heappop operation up to k times
SC: O(n)
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = [(-count,word) for word, count in Counter(words).items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]