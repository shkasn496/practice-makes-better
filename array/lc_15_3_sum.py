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

"""
Solution 2: Best solution, no set needed separately as well
TC: O(n^2)
SC: O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            # we dont want to re-compute duplicates, we already solved that
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
        return result