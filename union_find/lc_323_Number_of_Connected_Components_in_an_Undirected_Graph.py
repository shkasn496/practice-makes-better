# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
Solution 1: Recursive DFS
Success
Details 
Runtime: 99 ms, faster than 97.59% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
Memory Usage: 16.8 MB, less than 36.13% of Python3 online submissions for Number of Connected Components in an Undirected Graph.

TC: O(n+e)
SC: O(n+e)+log(n) Stack space
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adj_list = self.create_adjacency_list(n, edges)
        del edges
        def count_connected_components(curr_node, parent_node):
            if curr_node in visited:return True
            visited.add(curr_node)
            for ngbr in adj_list[curr_node]:
                if ngbr==parent_node:continue
                count_connected_components(ngbr,curr_node)
            return True
        count=0
        for node in range(n):
            if node not in visited:
                if count_connected_components(node, -1):
                    count+=1
        del visited, adj_list
        return count
        
    def create_adjacency_list(self, n, edges):
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

"""
Solution 2: Union Find

Runtime 100 ms Beats 94.61%
Memory 15.4 MB Beats 88.6%
TC: O(n+e)
SC: O(n+e)
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n==1:return 1
        uf = UnionFind(n)
        for (n1, n2) in edges:
            if uf.union(n1, n2):n-=1
        del uf
        return n
class UnionFind():
    def __init__(self, size):
        self.parent=[i for i in range(size)]
        self.rank=[0]*size
        return
    def find(self, x):
        if self.parent[x]==x:return x
        return self.find(self.parent[x])
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x==parent_y:return False
        if self.rank[parent_x]>=self.rank[parent_y]:
            self.parent[parent_y]=parent_x
            self.rank[parent_x]+=1
        else:
            self.parent[parent_x]=parent_y
            self.rank[parent_y]+=1
        return True