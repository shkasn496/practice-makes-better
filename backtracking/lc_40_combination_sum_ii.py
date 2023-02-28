# https://leetcode.com/problems/combination-sum-ii/description/
"""
Solution : Backtracking
Runtime 65 ms Beats 77.9%
Memory 14.1 MB Beats 17.32%
TC: O(2^N) because every step there is a choice to add or not add the number
SC: O(N)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i>idx and candidates[i]==candidates[i-1]:continue
                if candidates[i] > target:break
                backtrack(i+1, sum_arr+candidates[i], subarray+[candidates[i]])
            return
        backtrack(0, 0, [])
        return combinations