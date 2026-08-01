# https://leetcode.com/problems/remove-linked-list-elements/description/
"""
TC: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        curr = head
        prev = curr
        while curr:
            if curr.val != val:
                prev = curr
                curr = curr.next
            else:
                curr = curr.next
                prev.next = curr
        return head