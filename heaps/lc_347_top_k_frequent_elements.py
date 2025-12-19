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

"""
SOlution 2: Min Heap, is faster than max heap since we are only 
            storing k elements
"""
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store the frequencies of the elements
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        # use a minheap to get top K frequent elements
        minheap = []
        for n, freq in freq_map.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (freq, n))
            else:
                if freq > minheap[0][0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (freq, n))
        result = [elem[1] for elem in minheap]
        del minheap
        return result