# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
"""
Solution: Convert to Graph + Perform BFS traversal
Runtime 53 ms Beats 80.1%
Memory 14.4 MB Beats 27.6%

TC: O(N)+O(K)
SC: O(N+2^k)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return []
        if k==0:return [target.val]
        # convert tree to graph
        graph={}
        self.create_adjacency_list(root, graph)
        # perform BFS and stop BFS when level==k
        result=set()
        queue=Queue()
        queue.put((target.val,-1, 0))
        while not queue.empty():
            node, parent, level = queue.get()
            if level==k:result.add(node)
            if level>k:break
            for ngbr in graph[node]:
                if ngbr ==parent:continue
                queue.put((ngbr, node, level+1))
        del graph, queue
        return list(result)

    def create_adjacency_list(self, root, graph):
        if not root:return
        if root.val not in graph:
            graph[root.val]=[]
        if root.left: 
            graph[root.val].append(root.left.val)
            if root.left not in graph:
                graph[root.left.val]=[]
            graph[root.left.val].append(root.val)
        if root.right: 
            graph[root.val].append(root.right.val)
            if root.right not in graph:
                graph[root.right.val]=[]
            graph[root.right.val].append(root.val)
        self.create_adjacency_list(root.left, graph)
        self.create_adjacency_list(root.right, graph)
        return