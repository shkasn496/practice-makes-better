# https://leetcode.com/problems/merge-two-binary-trees/description/
"""
Solution 1: Recursion
Runtime 0 ms Beats 100.00%
Memory 18.13 MB Beats 34.81%

TC: O(n)
SC: O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
