# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
"""
Solution 1: Using DFS Preorder Traversal node->node.left->node.right
Runtime 130 ms Beats 48.42%
Memory 22.5 MB Beats 24.66%
TC:O(n)
SC:O(n) recursive stack
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
        if not root:return "#"
        return str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="#":return None
        data = data.split(',')
        self.i=0
        def dfs():
            if data[self.i]=='#':
                self.i+=1
                return None
            node=TreeNode(int(data[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
Solution 2: BFS Traversal
Runtime 256 ms Beats 5.5%
Memory 22.4 MB Beats 24.66%
TC:O(n)
SC:O(n)
"""
from queue import Queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:return "#"
        result = []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            result.append(str(node.val) if node else "#")
            if node and node.left:queue.put(node.left)
            elif node:queue.put(None)
            if node and node.right:queue.put(node.right)
            elif node:queue.put(None)
        del queue
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='#':return None
        data = data.split(',')
        root = TreeNode(val=int(data[0]))
        i=1
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if data[i]!='#':#left node
                node.left = TreeNode(val=int(data[i]))
                queue.put(node.left)
            else:node.left=None
            i+=1 # check for right node
            if data[i]!='#':#right node
                node.right = TreeNode(val=int(data[i]))
                queue.put(node.right)
            else:node.right=None
            i+=1 # update i for next node pointer
        del queue, data
        return root