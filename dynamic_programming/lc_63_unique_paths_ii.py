# https://leetcode.com/problems/unique-paths-ii/description/
"""
Solution 1: Dynamic programming with 2d array
Runtime 50 ms Beats 47.8%
Memory 14 MB Beats 38.36%
TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp=[[0]*n for i in range(m)]#2d array
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:continue
                if i==j==0:
                    dp[i][j]=1
                    continue
                if i>0 and obstacleGrid[i-1][j]!=1:
                    dp[i][j]+=dp[i-1][j] #up
                if j>0 and obstacleGrid[i][j-1]!=1:
                    dp[i][j]+=dp[i][j-1] #left
        unique_paths = dp[-1][-1]
        del dp
        return unique_paths

"""
Solution 2: Dynamic programming with 1d array
Runtime 46 ms Beats 66.72%
Memory 13.8 MB Beats 96.7%
TC: O(m*n)
SC: O(n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_dp=[0]*n
        prev_dp[0]=1 if obstacleGrid[0][0]!=1 else 0
        for i in range(m):
            temp_dp=[0]*n
            temp_dp[0]=prev_dp[0] if obstacleGrid[i][0]!=1 else 0
            for j in range(n):
                if obstacleGrid[i][j]==1:continue
                if i>0 and j>0 and obstacleGrid[i-1][j]!=1:
                    temp_dp[j]+=prev_dp[j] #up
                if j>0 and obstacleGrid[i][j-1]!=1:
                    temp_dp[j]+=temp_dp[j-1] #left
            prev_dp=temp_dp
            del temp_dp
        unique_paths = prev_dp[-1]
        del prev_dp
        return unique_paths