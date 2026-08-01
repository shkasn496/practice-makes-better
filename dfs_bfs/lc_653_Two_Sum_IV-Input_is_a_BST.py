# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
"""
Solution 1: inorder traversal + two pointers
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        # in order traversal
        def dfs(node, result):
            if not node: return
            left = dfs(node.left, result)
            result.append(node.val)
            right = dfs(node.right, result)
            return
        inorder = []
        dfs(root, inorder)
        l, r = 0, len(inorder) - 1
        while l < r:
            total = inorder[l] + inorder[r]
            if total == k:
                return True
            elif total > k:
                r -= 1
            else:
                l += 1
        del inorder
        return False
        