# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""
Solution 1: Preorder Traversal
TC : 
    serialize() -> O(N)
    deserialize() -> O(N)
SC :
    serialize() -> O(N)
    deserialize() -> O(N)    
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "N"
        def preorder(node):
            if not node: return ["N"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        return ",".join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "N" : return None
        data = data.split(",")
        self.idx = 0
        def preorder():
            node_val = data[self.idx]
            self.idx += 1
            if node_val == "N": return None
            node = TreeNode(val=int(node_val))
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))