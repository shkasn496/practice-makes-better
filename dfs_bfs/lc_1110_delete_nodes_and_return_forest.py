# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
"""
Solution 1: DFS Post Order Traversal
            Return None when node has to be deleted after adding children to 
            output
            Return node if node is not being deleted and no need to add 
            children to output
            Add root to the output if not being deleted
Runtime 53 ms Beats 100%
Memory 17 MB Beats 9.61%
TC: O(N)
SC: O(N) recursive stack + output
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if len(to_delete)==0:return [root]
        to_delete = set(to_delete)
        forest = []
        if root.val not in to_delete:forest.append(root)
        def dfs(node):
            if not node:return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left:forest.append(node.left)
                if node.right:forest.append(node.right)
                return None
            return node
        dfs(root)
        del to_delete
        return forest