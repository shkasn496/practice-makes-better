# https://leetcode.com/problems/number-of-islands-ii/description/
"""
Solution 1: Union Find with path compression using rank.
            Initialize parent groups with size m*n
            Maintain a visited set to get the lands added
Runtime 482 ms Beats 83.9%
Memory 21.8 MB Beats 45.48%
TC: O(m*n + p) where m*n for initializing the uf datastructure
                p is len(positions) for iterating over positions array
SC: O(m*n)
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        uf = UnionFind(m*n)
        lands_added=set()
        island_count=0
        res=[]
        for r,c in positions:
                if not (r,c) in lands_added:
                    lands_added.add((r,c))
                    island_count+=1
                    index_elem = r*n+c
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<m and 0<=nc<n and (nr,nc) in lands_added:
                            index_ngbr = nr*n+nc
                            island_count-= uf.union(index_elem, index_ngbr)
                res.append(island_count)
        del uf, directions, lands_added
        return res

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

"""
Solution 2: Time and Space Optimized!
             Instead of storing m*n values in uf.parent,
            just store the values of positions array and initialize to -1.
            No need to store a lands_added set as I can leverage the
            uf.parent states to identify if a land was added. 
            Crucial step is to mark the uf.parent[(r,c)]=(r,c) before checking
            any neighbors.

Runtime 533 ms Beats 38.33%
Memory 21.7 MB Beats 45.48%

TC: O(p + p) ~ O(p) as initialization of uf datastructure should take positions
                    array
SC: O(p)
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        uf = UnionFind(positions)
        island_count=0
        res=[]
        for r,c in positions:
            if uf.parent[(r,c)]==-1:
                uf.parent[(r,c)]=(r,c)
                island_count+=1
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not 0<=nr<m or not 0<=nc<n:continue
                    if (nr,nc) in uf.parent and uf.parent[(nr,nc)] != -1:
                        island_count-= uf.union((r,c), (nr,nc))
            res.append(island_count)
        del uf, directions
        return res

class UnionFind():
    def __init__(self, positions):
        self.parent = {(r,c): -1 for r,c in positions}
        self.rank = {(r,c): 0 for r,c in positions}
        return
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x==parent_y:return 0
        if self.rank[parent_x]>=self.rank[parent_y]:
            self.parent[parent_y]=parent_x
            self.rank[parent_x]+=1
        else :
            self.parent[parent_x]=parent_y
            self.rank[parent_y]+=1
        return 1