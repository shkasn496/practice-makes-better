# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
"""
Solution 1: DFS Post order traversal

Runtime 93 ms Beats 99.84%
Memory 31.9 MB Beats 22.81%

TC:O(N)
SC:O(N) recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root:return root
        nodes = set(nodes)
        def lca(node):
            if not node:return node
            left = lca(node.left)
            right = lca(node.right)
            if (node in nodes) or (left and right):return node
            return left or right
        result = lca(root)
        del nodes
        return result