# https://leetcode.com/problems/group-anagrams/description/
"""
Runtime 91 ms Beats 96.76%
Memory 17 MB Beats 95.65%

TC: O(n)*klog(k) k = len of substring
SC: O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:return [strs]
        count = collections.defaultdict(list)
        for i, s in enumerate(strs):
            count["".join(sorted(s))].append(s)
        return list(count.values())