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