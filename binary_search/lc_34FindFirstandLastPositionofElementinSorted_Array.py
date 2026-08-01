# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description

"""
TC: O(logN)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        n = len(nums)
        if nums[0]==nums[n-1]==target: return [0, n-1]
        def binary_search(left, right, isFirst):
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    if isFirst:
                        # find the start of the range
                        if mid == 0 or nums[mid-1] != target:
                            return mid
                        right = mid - 1
                    else:
                        # find the end of the range
                        if mid == n-1 or nums[mid+1] != target:
                            return mid
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        lower_bound = binary_search(0, n-1, isFirst=True)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = binary_search(0, n-1, isFirst=False)
        return [lower_bound, upper_bound]