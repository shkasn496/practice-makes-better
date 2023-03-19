# https://leetcode.com/problems/range-sum-of-bst/description/
"""
Solution 1: Using simple recursion
TC:O(n)
SC:O(n) stack space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:return 0
        rangeSum = root.val if low<=root.val<=high else 0
        return rangeSum+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)

"""
Solution 2: Using the property that the tree is Binary Search Tree (Optimal search)
Runtime 199 ms Beats 95.70% 
Memory 22.9 MB Beats 99.54%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:return 0
        rangeSum = root.val if low<=root.val<=high else 0
        if root.val > low:rangeSum+=self.rangeSumBST(root.left,low,high)
        if root.val < high:rangeSum+=self.rangeSumBST(root.right,low,high)
        return rangeSum