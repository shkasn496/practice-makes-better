"""
Solution 1: BFS - Store node and parent in the queue. Unclean solution, 
            adds tuples in queue

Runtime 3 ms Beats 11.46%
       
TC: O(n)
SC: O(W) where W is max width of the tree. (worst case, 2^H + 1 nodes, where H=logN)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = Queue()
        queue.put((root, None, 0))  # node, parent, depth
        x_info, y_info = None, None
        while not queue.empty():
            node, parent, depth = queue.get()
            if node.val == x:
                x_info = (parent, depth)
                if y_info:  # if y is found
                    return x_info[0] != y_info[0] and x_info[1] == y_info[1]
            elif node.val == y:
                y_info = (parent, depth)
                if x_info:  # if x is found
                    return x_info[0] != y_info[0] and x_info[1] == y_info[1]
            if node.left:
                queue.put((node.left, node, depth + 1))
            if node.right:
                queue.put((node.right, node, depth + 1))
        del queue
        return x_info[0] != y_info[0] and x_info[1] == y_info[1]


"""
Solution 2: Better solution, less queue space
            BFS - Store only node, check for siblings 
            and occurrence of cousins at next level
Runtime 0 ms Beats 100.00%
Memory 17.99 MB Beats 25.03%

TC: O(n)
SC: O(W) where W is max width of the tree. (worst case, 2^H + 1 nodes, where H=logN)
"""


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            level = queue.qsize()
            found_x = found_y = False

            for _ in range(level):
                node = queue.get()
                # check if next node are siblings
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (
                        node.left.val == y and node.right.val == x
                    ):
                        return False
                # Check for x and y at next level
                if node.left:
                    queue.put(node.left)
                    if node.left.val == x:
                        found_x = True
                    elif node.left.val == y:
                        found_y = True
                if node.right:
                    queue.put(node.right)
                    if node.right.val == x:
                        found_x = True
                    elif node.right.val == y:
                        found_y = True

            # Both are found at same level, and are not siblings
            if found_x and found_y:
                return True
            # Found one of the values at a level, and are not siblings
            if found_x or found_y:
                return False
        del queue
        return False
