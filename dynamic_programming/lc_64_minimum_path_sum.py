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
                if c==0:dp[r][c]+=dp[r-1][c]
                elif r==0:dp[r][c]+=dp[r][c-1]
                else:dp[r][c]+=min(dp[r][c-1], dp[r-1][c])#left,up
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
        m,n = len(grid), len(grid[0])
        dp=[0]*n#1d cache
        for r in range(m):
            temp_dp=[0]*n
            for c in range(n):
                temp_dp[c]=grid[r][c]
                if (r,c)==(0,0):continue
                if c==0:temp_dp[c]+=dp[c]
                elif r==0:temp_dp[c]+=temp_dp[c-1]
                else:temp_dp[c]+=min(temp_dp[c-1], dp[c])#left,up
            dp=temp_dp
        min_sum=dp[-1]
        del dp
        return min_sum
