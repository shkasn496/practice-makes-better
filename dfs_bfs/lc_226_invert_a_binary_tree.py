# https://leetcode.com/problems/invert-binary-tree/
"""
Success
Details 
Runtime: 39 ms, faster than 82.70% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 96.18% of Python3 online submissions for Invert Binary Tree.
TC: O(N)
SC: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        root.left, root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root