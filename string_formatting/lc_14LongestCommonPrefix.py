# https://leetcode.com/problems/longest-common-prefix/description/
"""
Solution1: Call zip(), then check each column

Runtime 27 ms Beats 98.95%
Memory 14 MB Beats 11.49%

TC: O(m) where m==largest word
SC: O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for elem in zip(*strs):
            if len(set(elem))!=1:break
            prefix+=elem[0]
        return prefix