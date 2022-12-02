# https://leetcode.com/problems/two-sum/description/

"""
Solution 1: Brute Force
Runtime 1209 ms Beats 26.75%
Memory 14.9 MB Beats 96.9%
TC: O(n^2)
SC: O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n2 = target - nums[i]
            if n2 in nums:
                try:
                    j = nums.index(n2)
                    if i!=j:return [i,j]
                except:continue
        return []

"""
Solution 2: Optimized solution
Runtime 58 ms Beats 97.81%
Memory 15.1 MB Beats 69.97%

TC : O(N)
SC : O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            n2 =target-nums[i]
            if n2 in pair and pair[n2]!= i:
                return [i, pair[n2]]
        return []