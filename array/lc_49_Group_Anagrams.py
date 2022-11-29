# https://leetcode.com/problems/group-anagrams/description/
"""
Runtime 98 ms Beats 96.80%
Memory 17.2 MB Beats 87.30%

TC: O(n)*klog(k) k = len of substring
SC: O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:return [strs]
        count = {}
        for i, s in enumerate(strs):
            s ="".join(sorted(s))
            if s in count:count[s].append(strs[i])
            else:count[s]=[strs[i]]
        return list(count.values())