# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution 1: Recursive DFS
Success
Details 
Runtime: 41 ms, faster than 96.31% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.3 MB, less than 54.72% of Python3 online submissions for Maximum Depth of Binary Tree.
TC: O(n)
SC : O(n)+ O(logn) (stack)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
Solution 2: Iterative DFS
Success
Details 
Runtime: 45 ms, faster than 91.82% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 90.04% of Python3 online submissions for Maximum Depth of Binary Tree.
TC: O(n)
SC : O(n)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDepth = 1
        stack = [(root,1)]
        while len(stack)>0:
            node, currDepth=stack.pop()
            if not node.left and not node.right:
                maxDepth=max(maxDepth, currDepth)
                continue
            if node.left:stack.append((node.left, currDepth+1))
            if node.right:stack.append((node.right, currDepth+1))
        del stack
        return maxDepth