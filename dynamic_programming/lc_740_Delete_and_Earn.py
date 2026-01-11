# https://leetcode.com/problems/delete-and-earn/description
"""
Solution 1: DP with tabulation
TC: O(n)
SC: O(max(nums))
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += num
        first = second = 0
        for num in freq:
            max_points = max(first + num, second)
            first = second
            second = max_points
        del freq
        return second