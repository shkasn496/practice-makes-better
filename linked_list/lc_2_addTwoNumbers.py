# https://leetcode.com/problems/add-two-numbers/description/
"""
Runtime 53 ms Beats 99.87%
Memory 14 MB Beats 10.46%

TC = SC = O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = ListNode()
        head = sum
        while l1 or l2:
            val=carry
            carry=0
            if l1: 
                val+=l1.val
                l1 = l1.next
            if l2: 
                val+=l2.val
                l2=l2.next
            carry = val // 10
            val = val % 10
            sum.val = val            
            if l1 or l2: 
                sum.next = ListNode()
                sum = sum.next

        if carry: sum.next = ListNode(val=carry)
        return head