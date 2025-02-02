# https://leetcode.com/problems/minimum-size-subarray-sum/
"""
Solution 1: Using sliding window with two pointers
TC: O(n)
SC: O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = len(nums) + 1
        i, j = 0, 0
        subarray_sum = 0
        while j < len(nums):
            if nums[j] + subarray_sum < target:
                subarray_sum += nums[j]
                j += 1
            else:
                min_subarray = min(min_subarray, j - i + 1)
                subarray_sum -= nums[i]
                i += 1
        return 0 if min_subarray == len(nums) + 1 else min_subarray
