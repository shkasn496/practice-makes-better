# https://leetcode.com/problems/permutations/description/
"""
Solution: Backtracking
Runtime 30 ms Beats 99.25% 
Memory 14.2 MB Beats 18.18%

TC: O(n!)
SC:O(n!)+O(n) recursive stack
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:return [nums]
        permutations=[]
        N=len(nums)
        def backtrack(used,subarray):
            # 1. Conditions
            if len(subarray)>N:return
            # 2. Goal
            if len(subarray)==N:
                permutations.append(subarray)
                return
            # 3. Choices
            for i in range(N):
                if i in used:continue
                used.add(i)
                backtrack(used, subarray+[nums[i]])
                used.remove(i)
            return
        backtrack(set(),[]) #cannot use subarray as set() because set doesnt store the order of addition
        return permutations