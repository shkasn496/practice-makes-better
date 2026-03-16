# https://leetcode.com/problems/diameter-of-n-ary-tree/description/
"""
Solution:
TC: O(n)
SC: O(n) recursive stack space
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root: return 0
        self.max_diameter = 0
        def dfs(node):
            if not node: return 0
            # left path is max path, right path is second max path
            node_left_path = node_right_path = 0
            for child in node.children:
                path = dfs(child)
                if path >= node_left_path:
                    node_right_path = node_left_path
                    node_left_path = path
                else:
                    node_right_path = max(node_right_path, path)
            self.max_diameter = max(self.max_diameter, node_left_path + node_right_path)
            return node_left_path + 1
        dfs(root)
        return self.max_diameter