# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""
Optimized solution
Runtime 94 ms Beats 81.32% 
Memory 21.3 MB Beats 95.21%
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.path_sum=-float("inf")
        def find_max_path_sum(node):
            if not node:return 0
            left_path_sum = max(0, find_max_path_sum(node.left))
            right_path_sum = max(0, find_max_path_sum(node.right))
            self.path_sum = max(self.path_sum, node.val+left_path_sum+right_path_sum)
            return node.val+max(left_path_sum, right_path_sum)
        find_max_path_sum(root)
        return self.path_sum