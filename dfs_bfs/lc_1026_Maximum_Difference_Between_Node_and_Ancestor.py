# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
"""
Solution 1: DFS - Goal is to find the min and max per subtree, choosing whether to take the value from the left subtree or the right subtree

Runtime 0ms Beats 100.00%
Memory 19.35MB Beats 67.09%

TC: O(n)
SC : O(H) where H stands for height of the tree for recursive stack
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_min, curr_max
            # Update the current value by visiting the node
            if node.val < curr_min:
                curr_min = node.val
            if node.val > curr_max:
                curr_max = node.val
            # Traverse its subtrees to get updated min and max values
            l_min, l_max = dfs(node.left, curr_min, curr_max)
            r_min, r_max = dfs(node.right, curr_min, curr_max)
            v_left = abs(l_min - l_max)
            v_right = abs(r_min - r_max)
            # return the min and max from the subtree with largest absolute diff
            if v_left >= v_right:
                return l_min, l_max
            return r_min, r_max

        l_min, l_max = dfs(root.left, root.val, root.val)
        r_min, r_max = dfs(root.right, root.val, root.val)
        v_left = abs(l_min - l_max)
        v_right = abs(r_min - r_max)
        return max(v_left, v_right)