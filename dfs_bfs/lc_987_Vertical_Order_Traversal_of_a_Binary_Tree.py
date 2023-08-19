# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
"""
Solution 1: Use BFS with a dict for storing all nodes part of a vertical column.
            Also store variables to get the min and max columns.
            Finally, sort the elements of the dict by the row numbers first, followed by the node val.

Runtime 30 ms Beats 99.24%
Memory 16.6 MB Beats 55.59%

TC:O(n) + O(klogk) where k=max elements part of column
SC:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        columns = defaultdict(list) # key:col, value: [(node.val, row_no)]
        queue = Queue()
        queue.put((root, 0, 0))
        min_col, max_col = 0, 0
        while not queue.empty():
            node, row, col = queue.get()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            columns[col].append((node.val, row))
            if node.left:queue.put((node.left, row+1, col-1))
            if node.right:queue.put((node.right,row+1, col+1))
        result = []
        for col in range(min_col, max_col+1):
            columns[col].sort(key=lambda elem: (elem[1], elem[0]))
            result.append([node for node, _ in columns[col]])
        del queue, columns
        return result