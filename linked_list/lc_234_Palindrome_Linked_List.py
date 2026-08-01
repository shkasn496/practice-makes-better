# https://leetcode.com/problems/palindrome-linked-list/description
"""
Solution : Optimized solution
TC: O(n)
SC: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return head
        slow = fast = head
        # find mid point at slow pointer
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        reversed_head = self.reverse_linkedlist(slow)
        while head and reversed_head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next
        return True
    
    def reverse_linkedlist(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev