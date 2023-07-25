# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""
Solution 1: BFS
Runtime 37 ms Beats 97.56%
Memory 16.6 MB Beats 31.46%
TC:O(n)
SC:O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        queue = Queue()
        queue.put(root)
        result = []
        level = 0
        while not queue.empty():
            nodes = queue.qsize()
            level += 1
            level_vals = []
            for _ in range(nodes):
                node = queue.get()
                level_vals.append(node.val)
                if node.left:queue.put(node.left)
                if node.right:queue.put(node.right)
            if level % 2 == 0: # even level from R -> L
                result.append(list(reversed(level_vals)))
            else: # odd level from L -> R
                result.append(level_vals)
        del queue
        return result

"""
Solution 2: DFS (most space optimized for balanced tree)
Runtime 26 ms Beats 97.7%
Memory 14 MB Beats 93.96%

TC: O(N)
SC: O(logN) for balanced tree
    O(N) for skewed tree
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        output = []
        def dfs(node, level):
            if not node:return
            while len(output)<=level:
                output.append([])
            output[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            return
        dfs(root,0)
        for level, lst in enumerate(output):
            if level%2 !=0: #odd level
                output[level]=reversed(lst)
        return output