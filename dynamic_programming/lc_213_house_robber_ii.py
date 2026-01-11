# https://leetcode.com/problems/house-robber-ii/description/
"""
Solution 1: DP with tabulation
TC: O(n)
SC: O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        rob_amt1 = self.rob1(nums[:-1])
        rob_amt2 = self.rob1(nums[1:])
        return max(rob_amt1, rob_amt2)

    def rob1(self, nums: List[int]) -> int:
            n = len(nums)
            if n < 2: return max(nums)
            first_house = second_house = 0
            for amt in nums:
                loot_amt = max(first_house + amt, second_house) # rob or leave unrobbed
                first_house = second_house
                second_house = loot_amt
            return loot_amt