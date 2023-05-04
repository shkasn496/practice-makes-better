# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
"""
Solution 1: DFS Post order traversal
Runtime 378 ms Beats 81.97%
Memory 69.7 MB Beats 16.31%
TC: O(n)
SC:O(n) recursive stack space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        self.max_sum = 0
        def dfs(node): # return isBST, min_val, max_val, BST_sum

            # null node should be considered a BST
            if not node:return (True, float('inf'), -float('inf'), 0)
            # leaf node is also BST
            if not node.left and not node.right:
                self.max_sum = max(self.max_sum, node.val)
                return (True, node.val, node.val, node.val)
            
            # post-order traversal 
            left_is_BST, left_min, left_max, left_sum = dfs(node.left)
            right_is_BST, right_min, right_max, right_sum = dfs(node.right)

            # if left and right children are BST, only then can the parent 
            # be a BST if left_child_max < parent < right_child_min
            if left_is_BST and right_is_BST and left_max < node.val < right_min:
                parent_sum = left_sum + node.val + right_sum
                self.max_sum = max(self.max_sum, parent_sum)
                return (True, min(left_min, node.val), max(node.val, right_max), parent_sum)
            
            # no conditions met, so return False
            return (False, float('inf'), -float('inf'), 0)
        dfs(root)
        return self.max_sum