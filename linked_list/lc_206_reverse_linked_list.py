# https://leetcode.com/problems/reverse-linked-list/description/
"""
Solution 1: Iterative
Runtime 0 ms Beats 100%
Memory 18.60MB Beats 25.74%
TC: O(n)
SC: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

"""
Solution 2: Recursive
Runtime 0 ms Beats 100%
Memory 19.02MB Beats 12.24%

TC: O(n)
SC: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive_helper(self, prev, head):
        if not head: return prev
        next_node = head.next
        head.next = prev
        return self.recursive_helper(head, next_node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        return self.recursive_helper(None, head)