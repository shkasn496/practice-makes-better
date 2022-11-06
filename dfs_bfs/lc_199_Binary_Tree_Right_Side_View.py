# https://leetcode.com/problems/binary-tree-right-side-view/

"""
Solution 1: BFS
Success
Details 
Runtime: 41 ms, faster than 83.31% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14 MB, less than 23.38% of Python3 online submissions for Binary Tree Right Side View.

TC: O(n)
SC:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        queue=Queue()
        queue.put(root)
        result=[]
        while not queue.empty():
            level=queue.qsize()
            for i in range(level):
                node=queue.get()
                if i==level-1:result.append(node.val)
                if node.left:queue.put(node.left)
                if node.right:queue.put(node.right)
        del queue
        return result

"""
Solution 2: Recursive DFS
Runtime: 40 ms Beats 85.45%
Memory: 14 MB Beats 23.37%
TC: O(n)
SC:O(n)+O(logN)(recursive stack)
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        result=[]
        def dfs(node, depth):
            if not node:return
            if len(result)>depth:result[depth]=node.val
            else: result.append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)
        return result