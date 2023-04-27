# https://leetcode.com/problems/closest-binary-search-tree-value/description/
"""
Solution 1: Binary search applied on BST

TC: O(H) where H=height of tree
        for balanced BST O(H)=O(logN)
        for skewed BST O(H)=O(N)
SC:O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:return 0
        closest_value = root.val
        while root:
            if abs(target - root.val) < abs(target-closest_value):
                closest_value = root.val
            elif abs(target - root.val) == abs(target-closest_value):
                closest_value=min(root.val,closest_value)
            if target < root.val:root=root.left
            else:root=root.right
        return closest_value