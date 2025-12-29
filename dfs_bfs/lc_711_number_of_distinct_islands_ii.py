# https://leetcode.com/problems/number-of-distinct-islands-ii/description/
"""
Solution 1: Solved using distance between all points of the island paths

"""
import math
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island_signature = set()
        directions = (-1, 0, 1, 0, -1) # up, right, down, left
        def dfs(r, c, start_r, start_c, island_path):
            grid[r][c]= 0 # mark as visited
            island_path.append((r-start_r, c-start_c))
            for dir in range(1, 5):
                nr = r + directions[dir-1]
                nc = c + directions[dir]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    dfs(nr, nc, start_r, start_c, island_path)
            return
        def get_island_distance(island_path):
            distance = []
            for i in range(len(island_path)):
                for j in range(i+1, len(island_path)):
                    pt1, pt2 = island_path[i], island_path[j]
                    x1, y1 = pt1
                    x2, y2 = pt2
                    dist = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
                    distance.append(dist)
            return sorted(distance)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    island_path = []
                    dfs(r, c, r, c, island_path)
                    distance = get_island_distance(island_path)
                    island_signature.add(tuple(distance))
        island_count = len(island_signature)
        del island_signature, directions
        return island_count