# https://leetcode.com/problems/boundary-of-binary-tree/description/
"""
Runtime 45 ms Beats 96.70%
Memory 16.5 MB Beats 30.64%

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
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        output = [root.val]
        def isLeaf(node):
            return node and (not node.left and not node.right)
        # define left boundary
        def left_boundary(node):
            if node and not isLeaf(node):
                output.append(node.val)
                if node.left:left_boundary(node.left)
                else:left_boundary(node.right)
        # define leaves boundary
        def leaves_boundary(node):
            if node:
                if isLeaf(node):
                    output.append(node.val)
                else:
                    leaves_boundary(node.left)
                    leaves_boundary(node.right)
        # define right boundary
        def right_boundary(node):
            if node and not isLeaf(node):
                if node.right:right_boundary(node.right)
                else:right_boundary(node.left)
                output.append(node.val)
        left_boundary(root.left)
        leaves_boundary(root.left)
        leaves_boundary(root.right)
        right_boundary(root.right)
        return output