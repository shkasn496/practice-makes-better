# https://leetcode.com/problems/validate-binary-search-tree/description/
"""
Solution 1: Check if the left and right subtrees satisfy the BST check
            by checking the minimum and maximum values of the subtrees
TC: O(n)
SC: O(n) recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def valid_check(node, minimum, maximum):
            if not node: return True
            if minimum >= node.val or maximum <= node.val:
                return False
            return valid_check(node.left, minimum, node.val) and \
                valid_check(node.right, node.val, maximum)
        return valid_check(root, -float("inf"), float("inf"))