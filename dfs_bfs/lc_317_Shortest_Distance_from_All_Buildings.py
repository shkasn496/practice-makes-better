# https://leetcode.com/problems/shortest-distance-from-all-buildings/description

"""
TC: O(n*m)^2
SC: O(n*m)
"""
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist_matrix = [[0]*n for _ in range(m)]
        directions = [(-1,0), (0,1), (1, 0), (0,-1)]
        def bfs(row, col):
            queue = deque([(row, col, 0)])
            land_dist = float("inf")
            while queue:
                r, c, curr_dist = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == LAND:
                        grid[nr][nc] -= 1 # mark land as visited
                        dist_matrix[nr][nc] += curr_dist + 1
                        queue.append((nr, nc, curr_dist + 1))
                        land_dist = min(land_dist, dist_matrix[nr][nc])
            return land_dist
        LAND = 0
        BUILDING = 1
        OBSTACLE = 2
        total_dist = float("inf")
        for r in range(m):
            for c in range(n):
                if grid[r][c] == BUILDING:
                    total_dist = bfs(r, c)
                    LAND -= 1
        del dist_matrix
        return total_dist if total_dist != float("inf") else -1