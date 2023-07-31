# https://leetcode.com/problems/merge-k-sorted-lists/
"""
Solution 1: Use minheap and store the elem val and list idx
Runtime 82 ms Beats 99.48%
Memory 20.2 MB Beats 47.20%
TC: O(nlogk)
SC:O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        minheap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(minheap, (l.val, idx))
                lists[idx]=lists[idx].next
        while minheap:
            val, idx = heapq.heappop(minheap)
            curr.next = ListNode(val=val)
            curr=curr.next
            if lists[idx]:
                heapq.heappush(minheap, (lists[idx].val, idx))
                lists[idx]=lists[idx].next
        del minheap
        return head.next