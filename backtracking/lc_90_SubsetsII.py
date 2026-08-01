https://leetcode.com/problems/subsets-ii/

"""
TC: O(NlogN) + O(N * 2^N)
SC: O(N * 2^N)
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        nums.sort()
        result = []
        def backtrack(idx, subset):
            result.append(subset)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, subset + [nums[i]])
            return
        backtrack(0, [])
        return result