# https://leetcode.com/problems/combination-sum-iii/description/
"""
Solution : Backtracking
Runtime 22 ms Beats 99.38%
Memory 13.8 MB Beats 70.20%
TC: O(K^N) # bot sure about this tbh
SC: O(K)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n==1 and k>n:return []
        result=set()
        def backtrack(idx,sum_values, sub_array):
            # conditions
            if sum_values>n or len(sub_array)>k:return
            # goal
            if sum_values==n and len(sub_array)==k:
                if tuple(sub_array) not in result:
                    result.add(tuple(sub_array))
                return
            # choices
            for i in range(idx,10):
                if i not in sub_array and len(sub_array) +1<=k:
                    sub_array.add(i)
                    sum_values+=i
                    backtrack(i+1, sum_values,sub_array )
                    sub_array.remove(i)
                    sum_values-=i
        backtrack(1,0,set())
        return result