# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
Solution 1: DFS post order traversal
Runtime 58 ms  Beats 97.4%
Memory 28.5 MB Beats 87.57%

TC:O(n)
SC:O(n) recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:return root
        return left or right