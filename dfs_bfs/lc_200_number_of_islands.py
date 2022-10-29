# https://leetcode.com/problems/number-of-islands/
"""
Solution 1: Use recursive DFS and store elem visited in a set
TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited=set()
        directions=[(0,1), (0,-1), (1,0), (-1,0)]
        island_count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n \
                or (r,c) in visited or grid[r][c]!="1":return 0
            visited.add((r,c))
            count=1
            for dr, dc in directions:
                count+=dfs(r+dr, c+dc)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    if dfs(r,c)>0: island_count+=1
        del visited, directions
        return island_count

"""
Solution 2: Use recursive DFS and modify elem visited in the grid
Success
Details 
Runtime: 302 ms, faster than 95.28% of Python3 online submissions for Number of Islands.
Memory Usage: 16.4 MB, less than 81.21% of Python3 online submissions for Number of Islands

TC: O(m*n)
SC: O(m+n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions=[(0,1), (0,-1), (1,0), (-1,0)]
        island_count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!="1":return 0
            grid[r][c] ="#"
            count=1
            for dr, dc in directions:
                count+=dfs(r+dr, c+dc)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    if dfs(r,c)>0: island_count+=1
        del directions
        return island_count