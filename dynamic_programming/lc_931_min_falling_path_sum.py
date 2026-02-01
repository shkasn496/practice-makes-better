# https://leetcode.com/problems/minimum-falling-path-sum/description/
"""
Solution 1: Recursive (DFS) with memoization. 
Runtime 198 ms Beats 17.94%
Memory 16.7 MB Beats 15.7%

TC: O(n^2) as matrix is nxn
SC:O(n^2)+O(n) for recursive stack
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions=[(1,0),(1,-1),(1,1)]
        dp={}
        def dfs(r, c):
            if not 0<=r<n or not 0<=c<n:return float("inf")
            if (r,c) in dp:return dp[(r,c)]
            if r==n-1:return matrix[r][c]
            ngbr_path=float("inf")
            for dr,dc in directions:
                ngbr_path = min(ngbr_path, dfs(r+dr,c+dc))
            dp[(r,c)]=ngbr_path+matrix[r][c]
            return dp[(r,c)]
        min_path_sum=float("inf")
        for i in range(n):
            min_path_sum=min(min_path_sum, dfs(0,i))
        del dp
        return min_path_sum

"""
Solution 2.a: Tabularization solution with 2d matrix
Runtime 127 ms Beats 90.12%
Memory 14.9 MB Beats 34.11%

TC: O(n^2) as matrix is nxn
SC:O(n^2)
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp=[[0]*n for _ in range(n)]
        dp[-1]=matrix[-1]#fill the last row
        for r in range(n-2,-1,-1):
            for c in range(n):
                dp[r][c]=matrix[r][c]
                if c==0:
                    dp[r][c]+=min(dp[r+1][c], dp[r+1][c+1])
                elif c==n-1:
                    dp[r][c]+=min(dp[r+1][c], dp[r+1][c-1])
                else:
                    dp[r][c]+=min(dp[r+1][c], min(dp[r+1][c-1], dp[r+1][c+1]))
        min_path_sum=min(dp[0])
        del dp
        return min_path_sum

"""
Solution 2.b: Space optimized Tabularization (BEST SOLUTION)
Runtime 121 ms Beats 96.63%
Memory 14.7 MB Beats 82.78%

TC: O(n^2) as matrix is nxn
SC:O(n)
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        bottom_dp=matrix[-1]#fill the last row
        for r in range(n-2,-1,-1):
            top_dp=[0]*n
            for c in range(n):
                top_dp[c]=matrix[r][c]
                if c==0:
                    top_dp[c]+=min(bottom_dp[c], bottom_dp[c+1])
                elif c==n-1:
                    top_dp[c]+=min(bottom_dp[c], bottom_dp[c-1])
                else:
                    top_dp[c]+=min(bottom_dp[c], min(bottom_dp[c-1], bottom_dp[c+1]))
            bottom_dp=top_dp
        min_path_sum=min(bottom_dp)
        del bottom_dp
        return min_path_sum

"""
Solution 4: Tabulation, but use the original matrix

TC: O(n ** 2)
SC: O(1)
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(1,n):
            for c in range(n):
                matrix[r][c] += min(matrix[r-1][max(0, c-1)],
                                matrix[r-1][max(0, c)],
                                matrix[r-1][min(n-1, c+1)]
                                )
        return min(matrix[-1])