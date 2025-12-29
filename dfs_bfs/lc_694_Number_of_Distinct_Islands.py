# https://leetcode.com/problems/number-of-distinct-islands/description/
"""
Solution 1: 

Runtime 231 ms Beats 88.47%
Memory 17.2 MB Beats 45.81%

TC: O(m*n)
SC: O(m*n) worst case if there is 1 island that is the entire grid
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island_signature = set()
        directions = (-1, 0, 1, 0, -1) # up, right, down, left
        path = []
        def dfs(r, c, start_r, start_c):
            if grid[r][c] == 0: return
            grid[r][c]= 0 # mark as visited
            path.append((r-start_r, c-start_c))
            for new_dir in range(1, 5):
                nr = r + directions[new_dir - 1]
                nc = c + directions[new_dir]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    dfs(nr, nc, start_r, start_c)
            return
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c, r, c)# (start_r, start_c) == (r, c)

                    island_signature.add(tuple(path))
                # clear the path for new island signature
                path.clear()
        distinct_islands = len(island_signature)
        del island_signature, directions, path
        return distinct_islands