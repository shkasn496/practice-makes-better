# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""
Solution 1: Using in order DFS - faster than BFS here since its a BST
Runtime 0 ms Beats 100.00%
Memory 19.21 MB Beats 61.76%

TC:O(n)
SC:O(logN) recursive stack space
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return (
            self.searchBST(root.left, val)
            if val < root.val
            else self.searchBST(root.right, val)
        )
