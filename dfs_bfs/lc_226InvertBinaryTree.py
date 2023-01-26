# https://leetcode.com/problems/invert-binary-tree/description/
"""
Solution 1: Recursion
Runtime 29 ms Beats 90.1% 
Memory 13.8 MB Beats 95.52%

TC:O(n)
SC:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return root
        root.left, root.right = root.right, root.left #swap children
         # call invert func on the swapped children to continue swaps on their children
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
Solution 2: Iterative solution (BFS)
Runtime 28 ms Beats 92.26%
Memory 14.1 MB Beats 8.81%

TC: O(n)
SC:O(n/2) because max no of elements in queue will be 
all leaves of last level i.e n/2 nodes of a full binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return root
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node=queue.get()
            node.left, node.right=node.right, node.left
            if node.left:queue.put(node.left)
            if node.right:queue.put(node.right)
        del queue
        return root
