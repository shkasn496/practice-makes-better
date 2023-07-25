# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""
Solution 1: Using a minheap
Runtime 510 ms Beats 83.60%
Memory 27.3 MB Beats 41.25%
TC: O(nlogK) where logK is for heappush operations which can happen n times
SC: O(k)
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k==1:return max(nums)
        minheap=[]
        for n in nums:
            if len(minheap)==k:
                if n <= minheap[0]:continue
                heapq.heappop(minheap)
            heapq.heappush(minheap, n)
        k_elem=minheap[0]
        del minheap
        return k_elem