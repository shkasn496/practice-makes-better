#https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
Success
Details 
Runtime: 34 ms, faster than 99.59% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.3 MB, less than 55.54% of Python3 online submissions for Search in Rotated Sorted Array.
TC:O(logn)
SC:O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        left, right = 0 , len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:return mid
            if nums[left]<=nums[mid]: #left space
                if nums[left]<=target<=nums[mid]:right=mid-1
                else:left=mid+1
            else: #right space
                if nums[mid]<=target<=nums[right]:left=mid+1
                else:right=mid-1
        return -1