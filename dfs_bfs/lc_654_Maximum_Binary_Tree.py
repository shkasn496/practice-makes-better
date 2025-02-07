"""
Solution 1: DFS preorder traversal
Runtime 37 ms Beats 37.09%
Memory 18.20 MB Beats 71.20%
TC: O(n^2)
SC:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def preorder(arr):
            if len(arr) == 0: # reached leaf
                return None
            idx = arr.index(max(arr))
            node = TreeNode(val=arr[idx])
            node.left = preorder(arr[:idx])
            node.right = preorder(arr[idx+1:])
            return node
        return preorder(nums)

"""
Solution 2: Using stack
Runtime 23 ms Beats 82.98%
Memory 18.04 MB Beats 85.31%
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = []
        for num in nums:
            node = TreeNode(val=num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()
            if nodes:
                nodes[-1].right = node
            nodes.append(node)
        root = nodes[0]
        del nodes
        return root