# https://leetcode.com/problems/combination-sum/description/
"""
Solution 1: Backtracking
Runtime 47 ms Beats 97.12%
Memory 14.1 MB Beats 9.25%

TC: O(N^T/M) where T is target, M is min value, N is list length
SC: O(T/M) in the last level of recursion
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==1 and target < candidates[0]:return []
        candidates.sort()
        result=set()
        def backtrack(idx, sub_array):
            sum_values=sum(sub_array)
            # conditions
            if sum_values>target:return
            # goal
            if sum_values==target:
                if tuple(sub_array) not in result:
                    result.add(tuple(sub_array))
                return
            # choices
            for i in range(idx,len(candidates)):
                if sum_values+candidates[i]<=target:
                    backtrack(i,sub_array+[candidates[i]])
        backtrack(0,[])
        return list(result)