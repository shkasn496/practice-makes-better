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
Runtime 27 ms Beats 94.11%
Memory 13.9 MB Beats 68.54%
TC:O(m*n)
SC:O(n)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_dp =[1]*n #cache 1d array
        for i in range(1,m):
            temp_dp=[0]*n
            temp_dp[0]=1
            for j in range(1,n):
                #up from prev_dp and left from temp_dp
                temp_dp[j]=prev_dp[j]+temp_dp[j-1]
            prev_dp=temp_dp
            del temp_dp
        cache = prev_dp[-1]
        del prev_dp
        return cache