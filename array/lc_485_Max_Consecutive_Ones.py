# https://leetcode.com/problems/max-consecutive-ones/description/
"""
Solution: Store two variables with curr and max counts
Runtime 327 ms Beats 94.99% 
Memory 16.8 MB Beats 16.45%
TC:O(n)
SC:O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = max_final = 0
        for num in nums:
            if num: max_ones+=1
            elif not num:
                max_final = max(max_ones, max_final)
                max_ones=0
        return max(max_ones, max_final)