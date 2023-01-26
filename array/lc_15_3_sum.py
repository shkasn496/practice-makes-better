# https://leetcode.com/problems/3sum/description/
"""
Solution Optimized:
TC:O(N^2)
SC:O(N)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:return []
        values = {nums[i]: i for i in range(len(nums))}
        result=set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                nums_k = -(nums[i]+nums[j])
                if nums_k not in values:continue
                k = values[nums_k]
                if i!=k and j!=k:
                    temp = tuple(sorted([nums[i], nums[j], nums_k]))
                    if temp not in result:
                        result.add(temp)
                    del temp
        del values
        return result