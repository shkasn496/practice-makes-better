# https://leetcode.com/problems/number-of-islands/
"""
Solution 1: Use recursive DFS and store elem visited in a set
TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited=set()
        directions=[(0,1), (0,-1), (1,0), (-1,0)]
        island_count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n \
                or (r,c) in visited or grid[r][c]!="1":return 0
            visited.add((r,c))
            count=1
            for dr, dc in directions:
                count+=dfs(r+dr, c+dc)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    if dfs(r,c)>0: island_count+=1
        del visited, directions
        return island_count

"""
Solution 2: Use recursive DFS and modify elem visited in the grid
Success
Details 
Runtime: 302 ms, faster than 95.28% of Python3 online submissions for Number of Islands.
Memory Usage: 16.4 MB, less than 81.21% of Python3 online submissions for Number of Islands

TC: O(m*n)
SC: O(m+n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions=[(0,1), (0,-1), (1,0), (-1,0)]
        island_count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!="1":return 0
            grid[r][c] ="#"
            count=1
            for dr, dc in directions:
                count+=dfs(r+dr, c+dc)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    if dfs(r,c)>0: island_count+=1
        del directions
        return island_count

"""
Solution 3: Union Find

Runtime 321 ms Beats 82.5%
Memory 20.3 MB Beats 37.66%

TC: O(m*n)
SC:O(m*n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0)]
        uf = UnionFind(m*n)
        island_count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c] =='0': continue
                island_count+=1
                index_elem = r*n+c
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                        index_ngbr = nr*n+nc
                        island_count-= uf.union(index_elem, index_ngbr)
        del uf, directions
        return island_count

class UnionFind():
    def __init__(self, size):
        self.groups = [i for i in range(size)]
        self.rank = [0]*size
        return
    def find(self, x):
        if self.groups[x]==x:return x
        return self.find(self.groups[x])
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x==parent_y:return 0
        if self.rank[parent_x]>=self.rank[parent_y]:
            self.groups[parent_y]=parent_x
            self.rank[parent_x]+=1
        else :
            self.groups[parent_x]=parent_y
            self.rank[parent_y]+=1
        return 1