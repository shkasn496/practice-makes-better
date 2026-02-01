# https://leetcode.com/problems/minimum-path-sum/description/
"""
Solution 1: Dynamic Programming Tabulation with 2D DP
Runtime 96 ms Beats 86.2%
Memory 15.6 MB Beats 80.77%

TC: O(m*n)
SC:O(m*n)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp=[[0]*n for _ in range(m)]#2d cache
        for r in range(m):
            for c in range(n):
                dp[r][c]=grid[r][c]
                if (r,c)==(0,0):continue
                if c == 0:
                    dp[r][c] += dp[r - 1][c]  # cumsum on first col
                elif r == 0:
                    dp[r][c] += dp[r][c - 1]  # cumsum on first row
                else:
                    dp[r][c] += min(dp[r][c - 1], dp[r - 1][c])  # check left, up
        min_sum=dp[m-1][n-1]
        del dp
        return min_sum

"""
Solution 2: 1D cache space optimzed (BEST SOLUTION)
Runtime 85 ms Beats 99.19%
Memory 14.7 MB Beats 95.75%

TC: O(m*n)
SC:O(n)
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev_row = [0]*n
        for r in range(m):
            curr_row = [0]*n
            for c in range(n):
                curr_row[c] = grid[r][c]
                if (r,c) == (0, 0): continue
                if c==0:
                    curr_row[c] += prev_row[c]
                elif r==0:
                    curr_row[c] += curr_row[c-1]
                else:
                    curr_row[c] += min(prev_row[c], curr_row[c-1])
            prev_row = curr_row
        min_path_sum = prev_row[-1]
        del prev_row
        return min_path_sum
