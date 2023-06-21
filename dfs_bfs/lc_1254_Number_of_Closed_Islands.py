# https://leetcode.com/problems/number-of-closed-islands/description/
"""
Solution 1: DFS traversal.
            if I come across a boundary cell r==(0, m-1) or c==(0,n-1),
            island is not surrounded by water. Hence return False and mark
            island as -2.
            If during dfs I dont come across any boundary cell or any previously
            visited -2 neighbour cells, return True and mark cell as 2.
Runtime 121 ms Beats 97.57%
Memory 17.1 MB Beats 27.65%

TC: O(m*n)
SC:O(m*n) for recursive stack space
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        closed_island_count = 0
        def is_closed(r,c):
            if r in {0,m-1} or c in {0,n-1}:
                grid[r][c]=-2
                return False #border cells
            grid[r][c]=2
            state=True
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0<=nr<m or not 0<=nc<n:continue
                if grid[nr][nc]==-2: # if ngbr is a visited boundary cell
                    state = False
                elif grid[nr][nc] == 0:
                    state = state and is_closed(nr, nc)
            # update the visited cell to -2 if the state returned is false
            if not state:grid[r][c]=-2
            return state
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    if is_closed(r,c):
                        closed_island_count+=1
        del directions
        return closed_island_count