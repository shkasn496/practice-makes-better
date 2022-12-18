# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

"""
Solution 1: DFS
Runtime 27 ms Beats 98.34%
Memory  13.8 MB  Beats 98.55%

TC: O(n)
SC: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        output = [] # indexes=levels of tree from bottom-up
        def dfs(node):
            if not node:return -1
            level = max(dfs(node.left), dfs(node.right))+1
            while len(output)<=level:
                output.append([])
            output[level].append(node.val)
            return level
        dfs(root)
        return output