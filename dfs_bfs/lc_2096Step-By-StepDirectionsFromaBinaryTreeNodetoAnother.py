# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

"""
Runtime 3930 ms Beats 23.35%
Memory 69 MB Beats 75.87%
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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = {}
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            curr = queue.get()
            if curr.val not in graph: graph[curr.val]=[]
            if curr.left:
                graph[curr.val].append((curr.left.val, 'L'))
                try: graph[curr.left.val].append((curr.val, 'U'))
                except:graph[curr.left.val]=[(curr.val, 'U')]
                queue.put(curr.left)
            if curr.right:
                graph[curr.val].append((curr.right.val, 'R'))
                try: graph[curr.right.val].append((curr.val, 'U'))
                except:graph[curr.right.val]=[(curr.val, 'U')]
                queue.put(curr.right)

        queue.put((startValue, -1, ""))
        while not queue.empty():
            curr, parent, path = queue.get()
            if curr==destValue:
                del queue, graph
                return path
            for (ngbr, step) in graph[curr]:
                if ngbr==parent:continue
                queue.put((ngbr, curr, path+step))
        del queue, graph
        return ""