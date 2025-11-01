# https://leetcode.com/problems/group-anagrams/description/
"""
Solution 1: Using sort
Runtime 13 ms Beats 55.53%
Memory 20.58 MB Beats 90.34%

TC: O(n*mlogm) where m = len of longest word
SC: O(n*m)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            ascii = "".join(sorted(word))
            if ascii not in groups:
                groups[ascii] = []
            groups[ascii].append(word)
        return list(groups.values())

"""
Solution 2: Using frequency count as signature (Faster)

TC: O(n * m)
SC: O(n * m)
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_count = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c) - ord('a')] += 1 # convert ascii to index
            freq_count[tuple(freq)].append(word)
        return list(freq_count.values())