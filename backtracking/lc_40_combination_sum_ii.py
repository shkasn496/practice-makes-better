# https://leetcode.com/problems/combination-sum-ii/description/
"""
Solution : Backtracking
Runtime 70 ms Beats 77.88% 
Memory 14.1 MB Beats 18.37%
TC: O(2^N) because every step there is a choice to add or not add the number
SC: O(N)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if target < candidates[0]:return []
        result=set()
        def backtrack(idx, sum_values, sub_array):
            # conditions
            if sum_values > target:return
            # goal
            if sum_values == target:
                if tuple(sub_array) not in result:
                    result.add(tuple(sub_array))
                return
            # choices
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i]==candidates[i-1]:
                    continue
                backtrack(i+1,sum_values+candidates[i], sub_array+[candidates[i]])
        backtrack(0,0,[])
        return result