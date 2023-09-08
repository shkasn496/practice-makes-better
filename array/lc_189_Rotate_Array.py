# https://leetcode.com/problems/rotate-array/description/

"""
Solution 1: Reverse the array. Then reverse first k and k onwards subarrays.

Runtime 171 ms Beats 93.92%
Memory 27.7 MB Beats 92.93%

TC:O(n)
SC:O(1)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:return
        # Reverse the entire array
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
        return