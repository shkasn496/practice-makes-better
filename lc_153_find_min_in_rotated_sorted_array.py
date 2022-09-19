#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Success
Details 
Runtime: 41 ms, faster than 95.74% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.1 MB, less than 62.95% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
TC: O(logn)
SC:O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #check if array is rotated, if not, then return first elem
        if not nums[0]>nums[-1]:return nums[0]
        # we established that nums is rotated.
        # nums[0] > nums[-1]. So, the minimum elem must be within this range
        left, right = 0, len(nums)-1
        while left < right:
            mid=left+(right-left)//2
            #check if minimum value is to the right of mid
            if nums[mid]>=nums[0]:
                if nums[mid]>nums[mid+1]:return nums[mid+1]
                left=mid+1
            #else minimum value is to left of mid
            else:right=mid
        return nums[right]