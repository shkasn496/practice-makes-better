# https://leetcode.com/problems/diameter-of-binary-tree/description/
"""
Solution: Recursion
Runtime 38 ms Beats 96.47%
Memory 16.2 MB Beats 76.30%
TC: O(n)
SC:O(n) Recursive stack
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
        self.diameter=0
        def longest_path(node):
            if not node:return 0
            left=longest_path(node.left)
            right=longest_path(node.right)
            self.diameter=max(self.diameter, left+right)
            return max(left,right)+1
        longest_path(root)
        return self.diameter