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
        l3=ListNode()
        head = l3
        carry=0
        while l1 or l2 or carry:
            num3=carry
            if l1:
                num3+=l1.val
                l1=l1.next
            if l2:
                num3+=l2.val
                l2=l2.next
            carry = num3 // 10
            l3.val = num3 % 10
            if l1 or l2 or carry: 
                l3.next=ListNode()
                l3=l3.next
        return head