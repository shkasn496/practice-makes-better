# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
"""
Solution 2: DFS+Memoization 
Runtime 432 ms Beats 94.51%
Memory 16.8 MB Beats 59.14%

TC: O(m*n). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once. 
The total time complexity is then O(V+E). V is the total number of vertices and E is the total number of edges. 
In our problem, O(V)=O(mn), O(E)=O(4V)=O(mn)
SC:O(m*n)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        dp=[[0]*n for r in range(m)]
        path = 0
        def dfs(r,c):
            if dp[r][c]!=0:return dp[r][c]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n or \
                matrix[nr][nc]<=matrix[r][c]:continue
                dp[r][c]=max(dp[r][c], dfs(nr, nc))
            dp[r][c]+=1
            return dp[r][c]
        for r in range(m):
            for c in range(n):
                path=max(path, dfs(r,c))
        del dp, directions
        return path

"""
Solution 1: Simple DFS
Gives Time Limit exceeded runtime error

TC: O(2^(m+n)) The search is repeated for each valid increasing path. In the worst case we can have O(2^{m+n}) calls.
SC: O(m*n)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        path = 0
        def dfs(r,c):
            path=0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n or \
                matrix[nr][nc]<=matrix[r][c]:continue
                path=max(path, dfs(nr, nc))
            return path+1
        for r in range(m):
            for c in range(n):
                path=max(path, dfs(r,c))
        return path