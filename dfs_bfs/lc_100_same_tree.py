# https://leetcode.com/problems/same-tree/

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
Runtime: 29 ms, faster than 97.11% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 75.45% of Python3 online submissions for Same Tree.
TC: O(n)
SC: O(n)+ O(logn) (recursive stack)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

"""
Solution 2: Iterative BFS
Success
Details 
Runtime: 39 ms, faster than 80.98% of Python3 online submissions for Same Tree.
Memory Usage: 14.1 MB, less than 29.00% of Python3 online submissions for Same Tree.
TC: O(n)
SC: O(n)
"""
from queue import Queue
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p and q):return p is q
        queue=Queue()
        queue.put((p,q))
        while not queue.empty():
            node1, node2 = queue.get()
            if not (node1 and node2) or node1.val != node2.val:return False
            # check left nodes
            if node1.left or node2.left:queue.put((node1.left, node2.left))
            # check right nodes
            if node1.right or node2.right:queue.put((node1.right, node2.right))
        del queue
        return True

"""
Solution 3: Iterative DFS
Success
Details 
Runtime: 37 ms, faster than 85.66% of Python3 online submissions for Same Tree.
Memory Usage: 13.8 MB, less than 75.45% of Python3 online submissions for Same Tree.
TC: O(n)
SC: O(n)+ O(logn) (recursive stack)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p and q):return p is q
        stack = [(p,q)]
        while len(stack)>0:
            node1, node2=stack.pop()
            if not (node1 and node2) or node1.val!=node2.val:return False
            if node1.left or node2.left: stack.append((node1.left, node2.left))
            if node1.right or node2.right: stack.append((node1.right, node2.right))
        del stack
        return True