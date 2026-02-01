# https://leetcode.com/problems/triangle/description/

"""
Solution 1: Bottom Up DP solution with memory saving

Runtime 0ms Beats 100.00%
Memory 18.43 MB Beats 99.76%

TC: O(N*M) where N is len(triangle)
SC: O(M) where M is len(triangle[-1])    
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[-1][-1]
        N = len(triangle)
        last_row = triangle[N-1]
        for r in range(N-2, -1, -1):
            for i in range(len(triangle[r])):
                last_row[i] = min(last_row[i], last_row[i+1]) + triangle[r][i]
        min_path_sum = last_row[0]
        del last_row
        return min_path_sum