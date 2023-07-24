# https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
Solution 1: Create a node map to store the new Nodes and point them to the 
            older nodes
Runtime 44 ms Beats 92.91%
Memory 17.2 MB Beats 73.55%
TC:O(n)
SC:O(n)
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        node_map = {head: Node(x=head.val)}
        placeholder = head
        while head:
            # Create next and random node addresses if not present
            if head.next and head.next not in node_map:
                node_map[head.next]= Node(x=head.next.val)
            if head.random and head.random not in node_map:
                node_map[head.random]= Node(x=head.random.val)
            # Point the head node's next and random to the created new addresses
            node_map[head].next = node_map.get(head.next, None)
            node_map[head].random = node_map.get(head.random, None)
            head=head.next
        copy_list = node_map[placeholder]
        del node_map
        return copy_list