# https://leetcode.com/problems/rotting-oranges/description/

"""
Solution 1: Use BFS

TC: O(m*n)
"""
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = Queue()
        fresh_oranges = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.put((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        if queue.empty(): return 0 if fresh_oranges == 0 else -1
        minutes = 0
        while not queue.empty() and fresh_oranges > 0:
            minutes += 1
            for _ in range(queue.qsize()):
                r, c = queue.get()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc] = 2 # orange turns rotten
                        fresh_oranges -= 1
                        queue.put((nr, nc))
        return minutes if fresh_oranges == 0 else -1