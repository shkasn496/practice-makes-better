# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
"""
Solution 1: Dfs / recursion
TC: O(n)
SC:O(n)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res


"""
Solution 2: Iterative
Runtime 40 ms Beats 95.10%
Memory 19.10 MB Beats 79.49%

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        del stack
        return res
