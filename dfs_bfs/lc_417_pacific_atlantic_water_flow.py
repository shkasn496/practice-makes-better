# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
Solution 1: Recursive DFS
Success
Details 
Runtime: 277 ms, faster than 97.00% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 17.5 MB, less than 9.30% of Python3 online submissions for Pacific Atlantic Water Flow.

TC: O((m+n)*(m*n))
SC:O(m*n)
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        if m==n ==1:return [(0,0)]
        pac, atl = set(), set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)] #east, west, south, north
        
        # check if cell can flow ocean water to next cell
        def dfs(r, c, ocean_visited):
            # add current cell to ocean
            ocean_visited.add((r,c))
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if 0<=new_r<m and 0<=new_c<n \
                and (new_r, new_c) not in ocean_visited \
                and heights[r][c]<=heights[new_r][new_c]: 
                    # height of current cell must be less 
                    #than or equal to adjacent cell for ocean 
                    #water to touch that cell (reverse of rain flowing to ocean)
                    dfs(new_r, new_c, ocean_visited)
            return
        
        # traverse left and right sides of grid to check
        # if ocean water reaches next cell
        for r1 in range(m):
            dfs(r1, n-1, atl)
            dfs(r1, 0, pac)
        # traverse top and bottom sides of grid to check
        # if ocean water reaches next cell
        for c1 in range(n):
            dfs(0, c1, pac)
            dfs(m-1, c1, atl)
        return atl & pac