# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
'''
Solution 1: dfs recursive post order traversal
Runtime 0 ms Beats 100.00%
Memory 17.74 MB Beats 49.48%
TC: O(n)
SC: O(n) call stack
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
'''
Solution 2: Iterative solution using stack
Runtime 0 ms Beats 100.00%
Memory 18.03 MB Beats 11.71%

TC: O(n)
SC : O(n)
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [(root, False)]
        result = []
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
                continue
            stack.append((node, True)) # Mark node as visited
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
        del stack
        return result