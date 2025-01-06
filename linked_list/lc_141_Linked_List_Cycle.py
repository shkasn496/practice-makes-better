# https://leetcode.com/problems/linked-list-cycle/description/
"""
Solution 1: Mark node as visited
Runtime 38ms Beats 93.33%
Memory 19.65 MB Beats 44.20%
TC: O(n)
SC: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        while head:
            if head.val is None: return True
            head.val = None # mark as visited
            head = head.next
        return False

"""
Solution 2: Two pointers
Runtime 48ms Beats 45.78%
Memory 19.73 MB Beats 36.87%

TC : O(n)
SC : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow: return True
        return False