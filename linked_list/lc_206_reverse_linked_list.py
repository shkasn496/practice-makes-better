# https://leetcode.com/problems/reverse-linked-list/description/
"""
Solution 1: Iterative
Runtime 31 ms Beats 93.37%
Memory 15.4 MB Beats 90.42%
TC: O(n)
SC:O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

"""
Solution 2: Recursive
Runtime 29 ms Beats 96.19%
Memory 20.5 MB Beats 6.47%
TC=SC=O(n)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev