# https://leetcode.com/problems/path-sum-ii/description/
"""
Runtime 49 ms Beats 90.12%
Memory 19.3 MB Beats 15.39%
TC: O(N^2)
SC:O(N^2)+logN recursive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def dfs(node, path, sumPath):
            if not node:return
            # encounter leaf node
            if not node.left and not node.right:
                if targetSum==sumPath+node.val: 
                    result.append(path+[node.val])
                return
            dfs(node.left, path+[node.val], sumPath+node.val)
            dfs(node.right, path+[node.val], sumPath+node.val)
            return
        dfs(root,[],0)
        return result