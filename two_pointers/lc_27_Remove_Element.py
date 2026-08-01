# https://leetcode.com/problems/remove-element/description
"""
TCL O(n)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left]!= val:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return left