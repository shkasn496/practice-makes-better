# https://leetcode.com/problems/number-of-distinct-islands/description/
"""
Solution 1: 

Runtime 231 ms Beats 88.47%
Memory 17.2 MB Beats 45.81%

TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        connected_island={}

        def dfs(r, c, idx):
            if r < 0 or c < 0 or r >= m or c >= n \
            or grid[r][c]==0 or grid[r][c]==-1:return False
            try: 
                # translate all other island rows and columns to the first row and column
                # store local coordinates instead of global coordinates
                r0, c0 = connected_island[idx][0]
                connected_island[idx].append((r-r0,c-c0))
            except: 
                connected_island[idx]=[]
                connected_island[idx].append((r,c))
            grid[r][c]*=-1
            for dr, dc in directions:
                dfs(r+dr, c+dc, idx)
            return True

        def check_unique_island(idx):
            if idx==0:return True
            for i in range(idx):
                if connected_island[i]==connected_island[idx]:return False
            return True

        idx = 0
        unique=0
        for r in range(m):
            for c in range(n):
                if dfs(r,c, idx):
                    #correcting first element of local coordinate of island
                    connected_island[idx][0]=(0,0)
                    if check_unique_island(idx): 
                        idx+=1
                        unique+=1
                    else: del connected_island[idx]
        del directions, connected_island
        return unique

"""
Solution 2: Optimized

Runtime 233 ms Beats 87.70%
Memory 17 MB Beats 54.29%

TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        connected_island=set()

        def find_island(r, c):
            if r < 0 or c < 0 or r >= m or c >= n \
            or grid[r][c]==0 or grid[r][c]==-1:return []
            grid[r][c]=-1 # mark as visited
            island_global_coords=[(r,c)]
            for dr, dc in directions:
                island_global_coords += find_island(r+dr, c+dc)
            return island_global_coords

        def convert_global_to_local_coords(island_coords):
            r0,c0 = island_coords[0]
            return tuple([(r-r0, c-c0) for (r, c) in island_coords])

        for r in range(m):
            for c in range(n):
                island_coords=find_island(r,c) #global coords
                if len(island_coords)==0:continue

                # convert global coords to local coords
                island_coords=convert_global_to_local_coords(island_coords) # stored as tuple

                if island_coords not in connected_island: # save local coord as hash func in set 
                    connected_island.add(island_coords)

        unique=len(connected_island)
        del directions, connected_island
        return unique