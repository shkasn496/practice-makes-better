# https://leetcode.com/problems/h-index/description
"""
Solution 1:
TC: O(nlogn) + O(n)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1: return 1 if citations[0] > 0 else 0
        citations.sort()
        max_h = 0
        curr_h = 0
        citation_idx = 0
        while citation_idx < n:
            if curr_h <= citations[citation_idx] and curr_h <= n - citation_idx:
                max_h = max(curr_h, max_h)
                curr_h += 1
            else:
                citation_idx += 1
        return max_h