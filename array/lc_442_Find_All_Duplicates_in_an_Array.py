# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""
Solution:
Runtime 397 ms Beats 88.11%
Memory 21.9 MB Beats 52.77%

TC: O(N)
SC : O(1)
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)<=1: return []
        duplicates=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx] <0:duplicates.append(idx+1)
            nums[idx]*=(-1)
        return duplicates