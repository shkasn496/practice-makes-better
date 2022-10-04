#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
Success
Details 
Runtime: 59 ms, faster than 90.56% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.5 MB, less than 19.84% of Python3 online submissions for Search in Rotated Sorted Array II.
TC: O(logn)
SC: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:return True
            elif nums[left]==nums[mid]==nums[right]:
                #bypass duplicates
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:
                # left space ascending order
                if nums[left]<=target<nums[mid]:right=mid
                else:left=mid+1
            else:
                # right space ascending order
                if nums[mid]<target<=nums[right]:left=mid+1
                else:right=mid
        return False