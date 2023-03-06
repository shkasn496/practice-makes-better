# https://leetcode.com/problems/shortest-path-to-get-food/description/
"""
Solution 1: BFS
Runtime 1007 ms Beats 5.40%
Memory 15.2 MB Beats 69.46%
TC: O(m*n)
SC:O(m*n)
"""
from queue import Queue
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        start_point=(0,0)
        for r in range(m):
            if not '*' in grid[r]:continue
            start_point = (r, grid[r].index('*'))
            break
        queue=Queue()
        queue.put((start_point[0], start_point[1], 0))
        while not queue.empty():
            r, c, step = queue.get()
            if grid[r][c]=='#':return step
            if grid[r][c] in {'X','|'}:continue
            grid[r][c]='|'#to not visit same location again
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n \
                or grid[nr][nc] in {'X','|'}:continue
                queue.put((nr, nc, step+1))
        del directions, queue
        return -1