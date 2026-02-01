# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/

"""
Solution 1: Space optimzied tabulation

TC: O(n ** 3)
SC: O(1)
"""
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for r in range(1, n):
            for c in range(n):
                min_non_zero_shift = float("inf")
                for i in range(n):
                    if i == c: continue
                    min_non_zero_shift = min(grid[r-1][i], min_non_zero_shift)
                grid[r][c] += min_non_zero_shift
        return min(grid[-1])