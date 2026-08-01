# https://leetcode.com/problems/single-element-in-a-sorted-array/description
"""
Solution : Binary Search
TC: O(logN)
SC: O(1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            halves_are_even = (right - mid) % 2 == 0
            if nums[mid+1] == nums[mid]:
                if halves_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid-1] == nums[mid]:
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        return nums[left]