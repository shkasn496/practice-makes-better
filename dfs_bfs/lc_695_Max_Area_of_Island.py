# https://leetcode.com/problems/max-area-of-island/description/
"""
Solution 1: Using DFS, and storing the visited islands in the input matrix

TC: O(m*n)
SC: O(m*n) recursive stack in worst case
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        def dfs(r, c):
            if grid[r][c] != 1: return 0
            grid[r][c]=0 # mark as visited
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<m and 0<=nc<n:
                    area += dfs(nr, nc)
            return area
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        return max_area