# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
Solution 1: Optimized solution using sliding window 
Runtime 89 ms Beats 82.52%
Memory 14 MB Beats 93.52%

TC: O(n)
SC:O(k) where k=max length of sliding window
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:return len(s)
        max_length = 0
        start= end = 0
        substring=set()
        while end < len(s):
            if s[end] not in substring:
                substring.add(s[end])
                end+=1
            else:
                substring.remove(s[start])
                start+=1
            max_length=max(len(substring), max_length)
        del substring
        return max_length