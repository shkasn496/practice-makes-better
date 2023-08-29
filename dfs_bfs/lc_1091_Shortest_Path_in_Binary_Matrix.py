# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""
Solution 1: BFS + mark cell as visited before adding element to queue for avoiding TLE

Runtime 782 ms Beats 21.27%
Memory 16.6 MB Beats 98.84%

TC:O(n)
SC:O(min_path)
"""
from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = Queue()
        queue.put((0, 0, 1))
        while not queue.empty():
            r, c, min_path = queue.get()
            if (r, c) == (n-1, n-1):return min_path
            grid[r][c]=1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc]=1 #mark as visited
                    queue.put((nr, nc, min_path+1))
        del queue, directions
        return -1