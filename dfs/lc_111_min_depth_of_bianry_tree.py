# https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
Runtime: 923 ms, faster than 61.08% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 54.6 MB, less than 53.45% of Python3 online submissions for Minimum Depth of Binary Tree.
TC: O(n)
SC: O(n)+ O(logn)(stack)
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        # return 1 if come across leaf node
        if not root.left and not root.right:return 1
        # if node has both sub-nodes
        elif root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # if node has one sub-node
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

"""
Solution 2: Iterative DFS
Success
Details 
Runtime: 741 ms, faster than 75.65% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.3 MB, less than 84.04% of Python3 online submissions for Minimum Depth of Binary Tree.
TC: O(n)
SC: O(n)+ O(logn)(stack)
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        mindepth=float("inf")
        stack=[(root, 1)]
        while len(stack)>0:
            node, currdepth = stack.pop()
            # encounter leaf node
            if not node.left and not node.right:
                mindepth=min(mindepth, currdepth)
                continue
            if node.left:stack.append((node.left, currdepth+1))
            if node.right:stack.append((node.right, currdepth+1))
        del stack
        return mindepth

"""
Solution 3: Iterative BFS (Fastest on average)
Success
Details 
Runtime: 568 ms, faster than 93.50% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.3 MB, less than 76.96% of Python3 online submissions for Minimum Depth of Binary Tree.
TC: O(n)
SC: O(n)
"""
from queue import Queue
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        queue=Queue()
        queue.put((root,1))
        while not queue.empty():
            node, currdepth = queue.get()
            # encounter leaf node, return currdepth
            if not node.left and not node.right:return currdepth
            if node.left:queue.put((node.left, currdepth+1))
            if node.right:queue.put((node.right, currdepth+1))
        del queue
        return