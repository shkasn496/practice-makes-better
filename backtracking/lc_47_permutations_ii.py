# https://leetcode.com/problems/permutations-ii/description/
"""
Solution
Runtime 356 ms Beats 22.65%
Memory 14.5 MB Beats 22.95%
TC=SC=O(n!)
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:return [nums]
        N=len(nums)
        permutations=set()
        def backtrack(used,subarray):
            # 2. Goal
            if len(subarray)==N:
                if tuple(subarray) not in permutations:
                    permutations.add(tuple(subarray))
                return
            # 3. Choices
            for i in range(N):
                if i in used:continue
                used.add(i)
                backtrack(used, subarray+[nums[i]])
                used.remove(i)
            return
        backtrack(set(), [])
        return permutations
    

"""
Solution 2: Better solution using hashmap
TC: O(n * n!)
"""
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        result, n = [], len(nums)
        def backtrack(counter, subset):
            if len(subset) == n:
                result.append(subset)
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(counter, subset + [num])
                    counter[num] += 1
            return
        backtrack(Counter(nums), [])
        return result