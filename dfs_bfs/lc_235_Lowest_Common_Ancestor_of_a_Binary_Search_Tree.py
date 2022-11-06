# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""
Runtime 71 ms Beats 99.37%
Memory 18.8 MB Beats 23.55%
TC: O(logN) Height of Tree average case
SC: O(logN) Recursive stack average case

TC: O(N) Height of Tree worst case for skewed tree
SC: O(N) Recursive stack worst case for skewed tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p < root < q: root is LCA because BST property
        if p.val > q.val: return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val <= q.val: return root
        if p.val < q.val < root.val : return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val < q.val : return self.lowestCommonAncestor(root.right, p, q)