# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
"""
Solution 1: Using BFS and hashmap and sorting
Runtime 28 ms Beats 95.96%
Memory 14 MB Beats 25.56%
TC: O(n)+O(nlogN)
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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        vertical_order=collections.defaultdict(list)
        queue=Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, col=queue.get()
            vertical_order[col].append(node.val)
            if node.left:queue.put((node.left, col-1))
            if node.right:queue.put((node.right, col+1))
        return [vertical_order[k] for k in sorted(vertical_order.keys())]

"""
Solution 2: BFS and no sorting (Time optimized better solution)
Runtime 33 ms Beats 82.24%
Memory 14.1 MB Beats 25.56%
TC: O(n)
SC: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        vertical_order=collections.defaultdict(list)
        min_col, max_col = 0,0
        queue=Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, col=queue.get()
            vertical_order[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:queue.put((node.left, col-1))
            if node.right:queue.put((node.right, col+1))
        return [vertical_order[k] for k in range(min_col, max_col+1)]