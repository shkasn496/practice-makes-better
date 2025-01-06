# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""
Solution 1: Recursive solution in one pass
Runtime 0ms Beats 100.00%
Memory 17.80MB Beats 16.92%

TC: O(n)
SC: O(n) Call stack space
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNode(curr):
            if not curr: return 0 # reached tail
            index = removeNode(curr.next) + 1
            if index == n + 1 : # reached node before the delete node
                curr.next = curr.next.next
            return index
        curr = head
        index = removeNode(curr)
        if index == n: # corner case when we need to remove the first element
            return head.next
        return head

"""
Solution 2: Iterative Solution
Runtime 0ms Beats 100.00%
Memory 17.68MB Beats 25.92%

TC: O(n)
SC: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        if n == len(stack): # remove first element
            del stack
            return head.next
        # replace pointers for the array element at node before delete node
        stack[-n-1].next = stack[-n-1].next.next
        del stack
        return head

"""
Solution 3: Best Solution, Iterative one pass with no additional memory
Runtime 0ms Beats 100.00%
Memory 17.68MB Beats 25.92%
TC : O(n)
SC : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n): fast = fast.next
        if not fast: return head.next # remove first element
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # replace pointers for the array element at node before delete node
        return head