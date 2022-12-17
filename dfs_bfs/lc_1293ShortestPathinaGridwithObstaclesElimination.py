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
        m, n = len(grid), len(grid[0])
        if k >= m+n-2:return m+n-2
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = Queue()
        queue.put((0,0,k,0))#r, c, k, steps
        visited = set()
        while not queue.empty():
            r, c, k, step = queue.get()
            if r==m-1 and c == n-1:return step
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr<m) and (0<=nc<n):
                    nk= k - grid[nr][nc]
                    if nk>=0 and (nr, nc, nk ) not in visited:
                        visited.add((nr, nc, nk))
                        queue.put((nr, nc, nk,step+1))
        del visited, queue, directions
        return -1