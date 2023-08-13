# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/
"""
Solution 1: DFS post order traversal with flags for p and q found
            First traverse the left and right subtrees, then check for p and q,
            then check lca condition.

Runtime 209 ms Beats 98.15%
Memory 30.1 MB Beats 82.39%

TC: O(N)
SC: O(N) recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_p = False
        self.found_q = False
        def LCA(node):
            # base condition
            if not node: return node
            # post order traversal
            left = LCA(node.left)
            right = LCA(node.right)
            # check if p or q is found
            if node==p or node==q:
                if node==p:self.found_p=True
                else: self.found_q=True
                return node
            # lca check
            if left and right:return node
            return left or right
        lca = LCA(root)
        return lca if self.found_p and self.found_q else None