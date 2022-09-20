#https://leetcode.com/problems/find-peak-element/
"""
Success
Details 
Runtime: 78 ms, faster than 47.84% of Python3 online submissions for Find Peak Element.
Memory Usage: 14 MB, less than 82.02% of Python3 online submissions for Find Peak Element.
TC: O(logn)
SC: O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if mid-1>=0 and mid+1<len(nums):
                if nums[mid-1]<nums[mid]>nums[mid+1]:return mid
                elif nums[mid-1]>nums[mid+1]:right=mid
                else:left=mid+1
            elif nums[left]>nums[right]:return left
            else:return right
        return left 