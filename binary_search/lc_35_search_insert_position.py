# https://leetcode.com/problems/search-insert-position/
"""
Runtime 0 ms Beats 100.00%
Memory 18.58 MB Beats 5.22%
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid]==target:return mid
            elif nums[mid]<target:
                low=mid+1
            else: high=mid-1
        return low