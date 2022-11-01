# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
Solution 1: Recursion Inorder traversal
Success
Details 
Runtime: 55 ms, faster than 92.64% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 89.08% of Python3 online submissions for Kth Smallest Element in a BST.

TC: O(n) worst case O(logN) average case for balanced tree height=logN
SC:  O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node):
            return inorder_traversal(node.left)+[node.val]\
        +inorder_traversal(node.right) if node else []
        return inorder_traversal(root)[k-1]