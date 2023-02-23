# https://leetcode.com/problems/merge-two-sorted-lists/description/
"""
Solution 1: Iterative solution
Runtime 31 ms Beats 95.58%
Memory 13.8 MB Beats 98.59%

TC: O(m+n)
SC:O(m+n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:return list1 if list1 else list2
        prev = prehead = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1=list1.next
            else:
                prev.next=list2
                list2=list2.next
            prev=prev.next
        prev.next=list1 or list2 #add leftover list
        return prehead.next