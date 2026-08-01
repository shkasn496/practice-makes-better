# https://leetcode.com/problems/squares-of-a-sorted-array/description
"""
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1: return [nums[0]**2]
        if nums[0] >= 0:
            return [num**2 for num in nums]
        new_nums = [0]* n
        left, right = 0, n-1
        idx = n-1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                new_nums[idx] = nums[right]**2
                right -= 1
            else:
                new_nums[idx] = nums[left]**2
                left += 1
            idx -= 1
        return new_nums