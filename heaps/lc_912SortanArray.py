# https://leetcode.com/problems/sort-an-array/description/

"""
Solution 1: Use minheap
Runtime 906 ms Beats 68.85%
Memory 22.3 MB Beats 47.77%
TC: O(nlogn)
SC:O(n)
"""
import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minheap = []
        for n in nums: heapq.heappush(minheap, n)
        i=0
        while minheap:
            nums[i] =heapq.heappop(minheap)
            i+=1
        del minheap
        return nums