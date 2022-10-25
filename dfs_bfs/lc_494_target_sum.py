# https://leetcode.com/problems/target-sum/

"""
Solution times out with error time limit exceeded

Solution 1: Basic DFS style recursion
TC: O(2^n) no. of nodes in a tree = 2^h - 1. Here h=len(nums)
SC: O(n)+O(log(n)) (recursive stack)
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums)==1:return 1 if nums[0]==abs(target) else 0
        def dfs(i, total):
            if i==len(nums): return 1 if total==target else 0
            return dfs(i+1, total+nums[i])+ dfs(i+1, total-nums[i])
        return dfs(0,0)

"""
Solution 2: Cache the sum of different ways for each index and total combination.
This reduces TC to O(t*n) where t=target and n=len(nums)

Success
Details 
Runtime: 375 ms, faster than 80.39% of Python3 online submissions for Target Sum.
Memory Usage: 36 MB, less than 29.19% of Python3 online submissions for Target Sum.

TC: O(t*n) where t=target and n=len(nums)
SC: O(n)+O(log(n)) (recursive stack)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums)==1:return 1 if nums[0]==abs(target) else 0
        cache = {} #key: (i, total) # value: count of sum-ways
        def dfs(i, total):
            if i==len(nums): return 1 if total==target else 0
            if (i,total) in cache: return cache[(i,total)]
            # add to cache
            cache[(i,total)] = dfs(i+1, total+nums[i])+ dfs(i+1, total-nums[i])
            return cache[(i,total)]
        return dfs(0,0)