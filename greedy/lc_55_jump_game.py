# https://leetcode.com/problems/jump-game/description/
"""
Solution 1: Greedy solution
Runtime 441 ms Beats 98.57%
Memory 17.8 MB Beats 15.11%
TC:O(n)
SC:O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        N=len(nums)
        curr_index_to_reach_last_index=N-1
        for i in range(N-2,-1,-1):
            jump=nums[i]
            if i+jump>=curr_index_to_reach_last_index:
                curr_index_to_reach_last_index=i
        return True if curr_index_to_reach_last_index==0 else False