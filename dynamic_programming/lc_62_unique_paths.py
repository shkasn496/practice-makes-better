# https://leetcode.com/problems/unique-paths/description/
"""
Solution 1: Optimized tabularization dp method
Runtime 23 ms Beats 98.65%
Memory 13.9 MB Beats 27.67%
TC:O(m*n)
SC:O(m*n)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[1]*n for i in range(m)]#cache 2d array
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]#up+left
        return dp[m-1][n-1]

"""
Solution 2: Further optimize space
Runtime 26 ms Beats 95.81%
Memory 13.8 MB Beats 68.54%
TC:O(m*n)
SC:O(n)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        prev_row = [1]*n
        max_paths = 0
        for r in range(1,m):
            curr_row = [0]*n
            curr_row[0] = 1
            for c in range(1, n):
                curr_row[c] = prev_row[c] + curr_row[c-1] # top and left values
            prev_row = curr_row
            max_paths = curr_row[-1]
        del prev_row
        return max_paths