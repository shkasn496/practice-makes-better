# https://leetcode.com/problems/clone-graph/

"""
Solution 1: recursive DFS
Success
Details 
Runtime: 38 ms, faster than 96.17% of Python3 online submissions for Clone Graph.
Memory Usage: 14.4 MB, less than 26.55% of Python3 online submissions for Clone Graph.
TC: O(N+E) E=edges
SC: O(N) N=nodes
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return None
        mapping={} # key: (node.val): value : new_node
        def dfs(curr_node):
            if curr_node is None:return None
            if curr_node.val in mapping: return mapping[curr_node.val]
            # create new node
            mapping[curr_node.val]=Node(val=curr_node.val)
            # link neighbors
            for ngbr in curr_node.neighbors:
                mapping[curr_node.val].neighbors.append(dfs(ngbr))
            return mapping[curr_node.val]
        # fill mapping dict
        dfs(node)
        return mapping[node.val]

"""
Solution 2: Iterative BFS

Success
Details 
Runtime: 45 ms, faster than 86.82% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 26.55% of Python3 online submissions for Clone Graph.
TC: O(n+v)
SC: O(n)
"""
from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return None
        mapping={node.val:Node(val=node.val)} # key: (node.val): value : new_node
        queue=Queue()
        queue.put(node)
        while not queue.empty():
            curr_node = queue.get()
            for ngbr in curr_node.neighbors:
            # link neighbors
                if ngbr.val not in mapping:
                    mapping[ngbr.val]=Node(val=ngbr.val)
                    queue.put(ngbr)
                mapping[curr_node.val].neighbors.append(mapping[ngbr.val])
                
        return mapping[node.val]