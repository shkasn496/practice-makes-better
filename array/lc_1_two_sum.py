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

"""
Solution 3: Further optimized solution by going through O(n) one time
Runtime 53 ms Beats 99.52%
Memory 15.2 MB Beats 25.98%

TC : O(N)
SC : O(N)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:return []
        dp={}
        # dp = {nums[i]:i for i in range(len(nums))} #key: elem, value: index of elem
        for i in range(len(nums)):
            num = target-nums[i]
            if num in dp and i!=dp[num]:
                return [i,dp[num]]
            dp[nums[i]]=i
        del dp
        return []