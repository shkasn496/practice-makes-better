# https://leetcode.com/problems/add-two-numbers/description/
"""
Runtime 53 ms Beats 99.87%
Memory 13.9 MB Beats 43.21%

TC = SC = O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:return l1 if l1 else l2
        l3 = ListNode()
        head = l3
        carry=0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            carry = val // 10 #quotient
            l3.val = val % 10 # remainder
            if l1 or l2 or carry:
                l3.next=ListNode()
                l3=l3.next
        return head