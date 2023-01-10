# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
"""
Solution 1: BFS
Runtime 41 ms Beats 61.47%
Memory 14.2 MB Beats 27.71%

TC: O(min(m, n)) where m and n are sizes of trees
SC: O(min(hm, hn)) where hm and hn are heights of trees
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:return True
        if not root1 or not root2 or root1.val != root2.val:return False
        queue1, queue2=Queue(), Queue()
        queue1.put((root1, -1))
        queue2.put((root2,-1))
        while not queue1.empty() and not queue2.empty():
            level1, level2=queue1.qsize(), queue2.qsize()
            # check to see if the number of nodes on a level are the same or not
            if level1!=level2:return False
            nodes1, nodes2 = {},{}
            for i in range(level1):
                (node1, parent1), (node2, parent2)=queue1.get(), queue2.get()
                nodes1[node1.val]=parent1
                nodes2[node2.val]=parent2
                if node1.left:queue1.put((node1.left,node1.val))
                if node1.right:queue1.put((node1.right,node1.val))
                if node2.left:queue2.put((node2.left,node2.val))
                if node2.right:queue2.put((node2.right,node2.val))
            # check to see if the nodes on same level have the same parent connection and same node values
            if nodes1 != nodes2:return False
        return queue1.qsize()==queue2.qsize()

"""
Solution 2: Recursion

Runtime 28 ms Beats 95.81%
Memory 13.8 MB Beats 76.25%

TC: O(min(m, n)) where m and n are sizes of trees
SC: O(min(hm, hn)) where hm and hn are heights of trees
"""
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:return True
        if not root1 or not root2 or root1.val != root2.val:return False
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
        self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)