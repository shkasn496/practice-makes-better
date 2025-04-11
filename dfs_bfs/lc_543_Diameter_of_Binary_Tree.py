# https://leetcode.com/problems/diameter-of-binary-tree/description/
'''
Solution 1: Save the largest diameter each time you come across a new node

Runtime 0 ms Beats 100.00%
Memory 20.91 MB Beats 21.27%

TC: O(n)
SC: O(H) recursive stack where H is height of the tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.diameter = 0
        def dfs(node):
            if not node: return 0
            left_edges = dfs(node.left)
            right_edges = dfs(node.right)
            self.diameter = max(self.diameter, left_edges + right_edges)
            return max(left_edges, right_edges) + 1
        dfs(root)
        return self.diameter