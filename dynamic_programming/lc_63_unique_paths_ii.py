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
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0
        prev_row = [0]* n
        prev_row[0] = 1 # start place
        for r in range(m):
            curr_row = [0]*n
            curr_row[0] = prev_row[0] if obstacleGrid[r][0]!= 1 else 0
            for c in range(n):
                if obstacleGrid[r][c] == 1: continue
                if r > 0 and c > 0 and obstacleGrid[r-1][c]!=1:
                    curr_row[c] += prev_row[c] # top
                if c > 0 and obstacleGrid[r][c-1] != 1:
                    curr_row[c] += curr_row[c-1] # left
            prev_row = curr_row
        max_paths = prev_row[-1]
        del prev_row
        return max_paths