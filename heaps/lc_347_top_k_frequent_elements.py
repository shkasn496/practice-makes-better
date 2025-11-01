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
            popping elements greater than k
"""
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        if len(count) == len(nums):return nums[:k] # case when m==N
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        result = [elem[1] for elem in min_heap]
        del count, min_heap
        return result