# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
Runtime 329 ms Beats 51.25%
Memory 15.7 MB Beats 46.79%

TC: O(m*n*k)
SC: O(m*n*k)
"""
from queue import Queue
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid), len(grid[0])
        # check if we can eliminate more obstacles that shortestPath
        if k>=m+n-2:return m+n-2
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()#row,col, k
        queue =Queue()
        queue.put((0,0,k,0))#row, col, k , step
        while not queue.empty():
            r, c, k, step=queue.get()
            if (r,c) == (m-1,n-1):return step
            if (r,c,k) in visited:continue
            visited.add((r,c,k))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n or (k<=0 and grid[nr][nc]==1):continue
                if k>0 and grid[nr][nc]==1:queue.put((nr,nc,k-1,step+1))
                elif grid[nr][nc]==0:queue.put((nr,nc,k,step+1))
        del queue, visited, directions
        return -1