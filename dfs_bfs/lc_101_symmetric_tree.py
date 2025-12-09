# https://leetcode.com/problems/symmetric-tree/

"""
Solution 1: Recursive DFS

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            return node1.val == node2.val and \
            dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root.left, root.right)

"""
Solution 2: Iterative DFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val: return False
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            elif node1 or node2: return False
        return True
    