# https://leetcode.com/problems/maximum-path-score-in-a-grid/description
"""
Solution: Memoization
TC: O(m*n*k)
SC:O(m*n*k)
"""
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cost = {0:0, 1:1, 2:1}
        # Base case for a 1x1 grid
        if (m,n) == (1,1):
            return grid[0][0] if cost[grid[0][0]] <= k else -1
        # 3D cache
        cache = [[[None] * (k+1) for _ in range(n)] for _ in range(m)]
        def dfs(r, c, curr_cost):
            if not (0<=r<m and 0 <=c<n):
                return -1
            curr_cost += cost[grid[r][c]]
            if curr_cost > k: return -1
            if (r, c) == (m-1, n-1):
                return grid[r][c]
            if cache[r][c][curr_cost] is not None:
                return cache[r][c][curr_cost]
            # right
            right = dfs(r, c+1, curr_cost)
            # down
            down = dfs(r+1, c, curr_cost)
            max_points = max(right, down)
            if max_points != -1:
                max_points += grid[r][c]
            cache[r][c][curr_cost] = max_points
            return cache[r][c][curr_cost]
        points = dfs(0, 0, 0)
        del cache
        return points
            