# https://leetcode.com/problems/house-robber/description/?
"""
Solution 1: DP with tabulation
TC:O(n)
SC:O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return max(nums)
        first_house = second_house = 0
        for amt in nums:
            loot_amt = max(first_house + amt, second_house) # rob or leave unrobbed
            first_house = second_house
            second_house = loot_amt
        return loot_amt 