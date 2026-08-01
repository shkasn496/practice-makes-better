# https://leetcode.com/problems/max-consecutive-ones-ii/description/
"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        left = right = 0
        max_length = 0
        flip_zero = False
        while right < len(nums):
            if nums[right] == 1:
                # expand the sliding window
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                if not flip_zero:
                    flip_zero = True
                    max_length = max(max_length, right - left + 1)
                    right += 1
                else:
                    # shrink the sliding window
                    flip_zero = False
                    while nums[left] != 0 and left <= right:
                        left += 1
                    if nums[left] == 0: left += 1
        return max_length