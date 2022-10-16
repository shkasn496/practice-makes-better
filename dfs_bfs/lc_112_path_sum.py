# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Success
Details 
Runtime: 39 ms, faster than 98.60% of Python3 online submissions for Path Sum.
Memory Usage: 15.2 MB, less than 15.53% of Python3 online submissions for Path Sum.
TC: O(n)
SC: O(n)+ O(logn) (stack)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        if root.left is None and root.right is None: return targetSum == root.val
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

"""
Solution 2: Iterative DFS
Success
Details 
Runtime: 45 ms, faster than 93.66% of Python3 online submissions for Path Sum.
Memory Usage: 15.1 MB, less than 56.50% of Python3 online submissions for Path Sum.
TC: O(n)
SC: O(n)+ O(logn) (stack)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        stack = [(root, targetSum-root.val)]
        while len(stack)>0:
            node, newSum = stack.pop()
            if node.left is None and node.right is None and newSum==0:return True
            if node.left:stack.append((node.left, newSum-node.left.val))
            if node.right:stack.append((node.right, newSum-node.right.val))
        del stack
        return False