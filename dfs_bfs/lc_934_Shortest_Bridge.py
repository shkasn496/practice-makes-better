# https://leetcode.com/problems/shortest-bridge/description/
"""
Solution 2: Same DFS structure. Only modification is on BFS calls where 
            I don't add a visited element back to the queue
            I also use the grid to track visited elems based on the foll enums:
            visited island1 cell = 2
            visited water cell = -2
            visited new land i.e island2 cell = -1
Runtime 506 ms Beats 17.51%
Memory 20.3 MB Beats 24.46%
TC:O(n^2)
SC:O(L) where L = size of island1
        O(L) for recursive stack space during DFS
        queue space will also be O(L) for BFS
"""
from queue import Queue
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        min_path = m*n
        # get island1 coordinates
        island1 = set()
        queue = Queue() # add island1 coords with min distance to island2 = 0
        def dfs(r,c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0<=nr<m or not 0<=nc<n or \
                not grid[nr][nc] or (nr,nc) in island1:continue
                island1.add((nr,nc))
                queue.put((nr,nc, 0))
                dfs(nr,nc)
            grid[r][c]=1 # completed visit
            return
        found=False
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    island1.add((r,c))
                    queue.put((r,c, 0))
                    dfs(r,c)
                    found=True
                    break
            if found:break
        # find the min distance between island1 and island2
        while not queue.empty():
            r, c, min_dist = queue.get()
            if not (r,c) in island1 and grid[r][c]==1:
                # found grid coord of island2
                min_path = min_dist
                break
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0<=nr<m or not 0<=nc<n or \
                (nr,nc) in island1:continue
                if not grid[nr][nc]: # found water
                    queue.put((nr,nc, min_dist+1))
                else: # found new island
                    queue.put((nr,nc, min_dist))
        del directions, island1, queue
        return min_path


"""
Solution 1: DFS to get the island1 coords + BFS to get min path from island1 to island2
            This solution will work but will give TLE as there are 
            multiple BFS nodes added to queue which had previously been calculated.

"""
from queue import Queue
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        min_path = m*n
        # get island1 coordinates
        island1 = set()
        queue = Queue() # add island1 coords with min distance to island2 = 0
        def dfs(r,c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0<=nr<m or not 0<=nc<n or \
                not grid[nr][nc] or (nr,nc) in island1:continue
                island1.add((nr,nc))
                queue.put((nr,nc, 0))
                dfs(nr,nc)
            grid[r][c]=1 # completed visit
            return
        found=False
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    island1.add((r,c))
                    queue.put((r,c, 0))
                    dfs(r,c)
                    found=True
                    break
            if found:break
        # find the min distance between island1 and island2
        while not queue.empty():
            r, c, min_dist = queue.get()
            if not (r,c) in island1 and grid[r][c]==1:
                # found grid coord of island2
                min_path = min_dist
                break
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0<=nr<m or not 0<=nc<n or \
                (nr,nc) in island1:continue
                if not grid[nr][nc]: # found water
                    queue.put((nr,nc, min_dist+1))
                else: # found new island
                    queue.put((nr,nc, min_dist))
        del directions, island1, queue
        return min_path