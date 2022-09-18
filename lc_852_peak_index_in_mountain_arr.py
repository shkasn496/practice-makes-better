#https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
Success
Details 
Runtime: 624 ms, faster than 95.69% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 27.8 MB, less than 63.90% of Python3 online submissions for Peak Index in a Mountain Array.
TC: O(logn)
SC: O(1)
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left<right:
            mid = left + (right-left)//2
            if arr[mid]<arr[mid+1]:left=mid+1
            else:right=mid
        return right