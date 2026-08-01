# https://leetcode.com/problems/lru-cache/description/
"""
Solution
"""
class Node:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {} # key -> value points to a node in Doubly LL
        self.head = Node() # holds end node in Doubly LL
        self.tail = Node() # holds latest node in Doubly LL
        self.head.right = self.tail
        self.tail.left = self.head
    
    def _add_to_tail(self, curr_node):
        latest_node = self.tail.left
        # add curr_node after latest node
        latest_node.right = curr_node
        curr_node.left = latest_node
        curr_node.right = self.tail
        # update latest tail node pointer
        self.tail.left = curr_node
        return

    def _remove_node(self, node):
        node.left.right = node.right
        node.right.left = node.left
        return
    
    def get(self, key: int) -> int:
        if len(self.keys) == 0 or key not in self.keys: return -1
        curr_node = self.keys[key]
        self._remove_node(curr_node)
        self._add_to_tail(curr_node)
        return curr_node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            old_node = self.keys[key]
            self._remove_node(old_node)
            del self.keys[key]

        # update latest tail node pointer
        curr_node = Node(key=key, val=value)
        self.keys[key] = curr_node
        self._add_to_tail(curr_node)
        
        if len(self.keys) > self.capacity:
            del_node = self.head.right
            self._remove_node(del_node)
            del self.keys[del_node.key]