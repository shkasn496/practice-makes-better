# https://leetcode.com/problems/shortest-path-in-binary-matrix/description

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1: return 1 if grid[0][0]==0 else -1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0: return -1
        queue = deque([(0,0,1)])
        grid[0][0] = 1 # mark as visited
        directions = [(-1,0), (0,1),(1,0),(0,-1), (-1, 1), (1,-1), (-1,-1),(1,1)]
        while queue:
            r, c, dist = queue.popleft()
            if (r,c) == (n-1, n-1): return dist
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                    grid[nr][nc] = 1 # mark as visited
                    queue.append((nr, nc, dist+1))
        del queue, directions
        return -1