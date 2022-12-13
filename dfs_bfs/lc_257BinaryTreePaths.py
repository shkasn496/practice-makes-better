# https://leetcode.com/problems/binary-tree-paths/description/
"""
Solution 1: DFS
Runtime 36 ms Beats 90.6%
Memory 14 MB Beats 31.41%

TC: O(n)
SC : O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:return []
        paths=[]
        def dfs(node, path):
            if not node:return
            path+=str(node.val)
            if not node.left and not node.right: #leaf
                paths.append(path)
            else:
                dfs(node.left, path+"->")
                dfs(node.right, path+"->")
            return
        dfs(root, "")
        return paths

