# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
"""
Solution 1: Traverse tree and consider each node to either continue the path 
            or start a new path
Runtime 363 ms Beats 91.88%
Memory 63.9 MB Beats 8.24%
TC:O(n)
SC:O(n) recursive stack space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.max_path = 0
        def dfs(node, goLeft, path):
            if not node:return
            if goLeft:
                dfs(node.left, not goLeft, path+1)
                dfs(node.right, goLeft, 1)
            else:
                dfs(node.right, not goLeft, path+1)
                dfs(node.left, goLeft, 1)
            self.max_path = max(self.max_path, path)
            return
        dfs(root, True, 0)
        return self.max_path

"""
Solution 2: Cleaner and faster solution. Reduces no. of function calls.
Runtime 349 ms Beats 97.23%
Memory 64.2 MB Beats 7.87%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.max_path = 0
        def dfs(node, goLeft, path):
            if not node:return
            if node.left:
                dfs(node.left, False, path+1 if goLeft else 1)
            if node.right:
                dfs(node.right, True, path+1 if not goLeft else 1)
            self.max_path = max(self.max_path, path)
            return
        dfs(root, True, 0)
        return self.max_path