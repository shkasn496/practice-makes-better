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
        if len(s)<2:return len(s)
        start,end=0,1
        substring=set()
        substring.add(s[start])
        maxlength=1
        while end<len(s):
            if s[end] in substring:
                substring.remove(s[start])
                start+=1
            else:
                substring.add(s[end])
                end+=1
            maxlength=max(maxlength, len(substring))
        del substring
        return maxlength