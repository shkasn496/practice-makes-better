# https://leetcode.com/problems/graph-valid-tree/
"""
Solution 1: Recursive DFS for cycle detection
Success
Details 
Runtime: 97 ms, faster than 94.38% of Python3 online submissions for Graph Valid Tree.
Memory Usage: 17.1 MB, less than 27.87% of Python3 online submissions for Graph Valid Tree.

TC: O(n+e)
SC: O(n+e)+log(n) (stack)
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n>1 and len(edges)<n-1:return False
        adj_list = self.create_adjacency_list(n, edges)
        del edges
        visited=set()
        
        # check for cycle
        def cycle_detected(curr_node, parent_node):
            if curr_node in visited and curr_node != parent_node:
                return True
            visited.add(curr_node)
            for ngbr in adj_list[curr_node]:
                if ngbr==parent_node:continue
                if cycle_detected(ngbr, curr_node):
                    return True
            return False
        
        # traverse all nodes
        for node in range(n):
            if node not in visited:
                if cycle_detected(node, -1):
                    return False
        del adj_list
        return len(visited)==n # handle any missing node that wasn't visited because there was no edge
        
    def create_adjacency_list(self, n, edges):
        adj_list={i:[] for i in range(n)}
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

"""
Solution 2: Union Find

Runtime 91 ms Beats 96.15%
Memory 15.3 MB Beats 91.30%

TC: O(e+n) where e=len(edges), n =no of nodes
SC: O(n)
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:return True
        if n-1 !=len(edges):return False
        uf = UnionFind(n)
        for (n1,n2) in edges:
            # if two nodes have same parent before calling union, there is a cycle
            if uf.find(n1)==uf.find(n2):return False #check for cycle
            uf.union(n1, n2)
            n-=1
        del uf
        return n==1

class UnionFind():
    def __init__(self, size):
        self.parent=[i for i in range(size)]
        self.rank = [0]*size
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