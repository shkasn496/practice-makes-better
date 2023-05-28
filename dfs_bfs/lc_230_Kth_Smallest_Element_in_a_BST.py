# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
Solution 1: Recursion Inorder traversal
Success
Details 
Runtime: 55 ms, faster than 92.64% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 89.08% of Python3 online submissions for Kth Smallest Element in a BST.

TC: O(n) to build traversal
SC:  O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node):
            return inorder_traversal(node.left)+[node.val]\
        +inorder_traversal(node.right) if node else []
        return inorder_traversal(root)[k-1]

"""
Solution 2: Better optimized inorder traversal. Only traversing height of tree.
Runtime 55 ms Beats 72.97%
Memory 20.5 MB Beats 18.96%
TC:O(logN+k) Balanced Tree
    O(N + k) skewed tree with all the nodes in the left subtree.
SC: O(k) + O(H) output array + recursive stack for height of tree
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        def inorder_traversal(node):
            if not node:return
            if node.left:inorder_traversal(node.left)
            if len(stack)<k:stack.append(node.val)
            if len(stack)<k:inorder_traversal(node.right)
            return
        inorder_traversal(root)
        k_smallest=stack[-1]
        del stack
        return k_smallest