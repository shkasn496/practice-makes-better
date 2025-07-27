# https://leetcode.com/problems/deepest-leaves-sum/description/

"""
Solution 1: Simple DFS, use global variables to save max_sum and max_depth
TC: O(n)
SC: O(1) for variables + O(H) for recursive stack space
"""
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.max_depth, self.max_sum = 0, 0
        def dfs(node, depth):
            if not node: return
            if not node.left and not node.right: # leaf
                if depth == self.max_depth:
                    self.max_sum += node.val
                elif depth > self.max_depth:
                    self.max_depth = depth
                    self.max_sum = node.val
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return
        dfs(root, 0)
        return self.max_sum

"""
Solution 2: DFS, but this time, bubble up the max_sum from the subtrees instead of storing in a global variable

TC: O(n)
SC: O(1) for variables + O(H) for recursive stack space
"""
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node, depth):
            if not node: return None
            if not node.left and not node.right: # leaf
                return node.val, depth
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if not left or not right:
                return left or right
            if left[1] > right[1]:
                return left
            elif left[1] < right[1]:
                return right
            return left[0] + right[0], left[1]
        max_sum, max_depth = dfs(root, 0)
        return max_sum

"""
Solution 3: BFS

TC: O(n)
SC: O(n) for queue space max last level nodes
"""
from queue import Queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = Queue()
        queue.put(root)
        max_sum = 0
        while not queue.empty():
            level = queue.qsize()
            total = 0
            for _ in range(level):
                node = queue.get()
                total += node.val
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            max_sum = total
        del queue
        return max_sum