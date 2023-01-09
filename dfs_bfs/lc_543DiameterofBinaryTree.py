# https://leetcode.com/problems/diameter-of-binary-tree/description/
"""
Solution: DFS

Runtime 43 ms Beats 92.52%
Memory 16.2 MB Beats 82.70%
TC: O(n)
SC:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.max_diameter=0
        def dfs(node):
            if not node:return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            node_max_height=1+max(left_height, right_height)
            self.max_diameter=max(left_height+right_height, self.max_diameter)
            return node_max_height
        dfs(root)
        return self.max_diameter