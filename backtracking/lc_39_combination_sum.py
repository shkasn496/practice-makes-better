# https://leetcode.com/problems/combination-sum/description/
"""
Solution 1: Backtracking
Runtime 46 ms Beats 97.34%
Memory 14.3 MB Beats 8.54%
TC: O(N^T/M) where T is target, M is min value, N is list length
    every step there is a choice to add the number 0-N times 
    which is why it is N raised to T instead of 2 ^ T.

SC: O(T/M) in the last level of recursion
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==1 and target>candidates[0]:return []
        N = len(candidates)
        candidates.sort()
        combinations = set()
        def backtrack(idx, sum_arr, subarray):
            # 1. Conditions
            if idx > N or sum_arr>target:return
            # 2. Goal
            if sum_arr==target:
                comb=tuple(subarray)
                if comb not in combinations:
                    combinations.add(comb)
                del comb
                return
            # 3. Choices
            for i in range(idx, N):
                if sum_arr+candidates[i]<=target:
                    backtrack(i, sum_arr+candidates[i], subarray+[candidates[i]])
            return
        backtrack(0, 0, [])
        return combinations