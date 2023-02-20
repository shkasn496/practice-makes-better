# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""
Solution 1: BFS
Runtime 33 ms Beats 75.86%
Memory 14.3 MB Beats 10.16%
TC: O(n)
SC: O(2*L) where L = level. At most, we will have 2 levels of nodes in the queue.
At leaf level for a balanced tree, L = N/2 
So, worst case SC= O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        output = []
        queue = Queue()
        queue.put((root,0))#node, level 
        while not queue.empty():
            node, level = queue.get()
            while len(output)<=level:
                output.append([])
            output[level].append(node.val)
            if node.left: queue.put((node.left, level+1))
            if node.right: queue.put((node.right, level+1))
        for level, lst in enumerate(output):
            if level%2 !=0: #odd level
                output[level]=reversed(lst)
        del queue
        return output

"""
Solution 2: DFS (most space optimized for balanced tree)
Runtime 26 ms Beats 97.7%
Memory 14 MB Beats 93.96%

TC: O(N)
SC: O(logN) for balanced tree
    O(N) for skewed tree
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        output = []
        def dfs(node, level):
            if not node:return
            while len(output)<=level:
                output.append([])
            output[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            return
        dfs(root,0)
        for level, lst in enumerate(output):
            if level%2 !=0: #odd level
                output[level]=reversed(lst)
        return output