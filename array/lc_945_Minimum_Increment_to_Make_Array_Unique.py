# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
"""
Solution 1: Sort first. Save prev as biggest number seen so far. minMoves += prev- curr + 1

Runtime 852 ms Beats 97.8%
Memory 28.6 MB Beats 40.73%

TC : O(nlogn)
SC: O(1)
"""
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums)<=1: return 0
        nums.sort()
        prev=nums[0] #holds largest no seen so far
        minIncrements=0
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr <= prev: # we need to change curr
                minIncrements+=prev-curr+1
                curr=prev+1
            prev = curr
        return minIncrements