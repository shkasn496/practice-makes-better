# https://leetcode.com/problems/subsets/description/

"""
TC: O(N * 2^N)
SC: O(N * 2^N)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        result = []
        def backtrack(idx, subset):
            result.append(subset)
            for i in range(idx, len(nums)):
                backtrack(i+1, subset + [nums[i]])
            return
        backtrack(0, [])
        return result