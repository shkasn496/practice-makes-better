# https://leetcode.com/problems/custom-sort-string/description/
"""
Solution 1: First iterate over all chars present in order and add their freq to the result.
            Next, whatever freq is left in string_count that isn't zero, add to the result.

Runtime 29 ms Beats 98.16%
Memory 16.2 MB Beats 70.39%

TC:O(m+n) where m=len(order), n = len(string)
SC:O(m+n) for order dict and string count dict
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = {i:c for i, c in enumerate(order)}
        string_count = collections.Counter(s)
        priority = 0
        result = []
        while priority < len(order):
            curr_char = order[priority]
            if curr_char in string_count:
                result.append(curr_char * string_count[curr_char])
                string_count[curr_char]=0
            priority+=1
        for c, f in string_count.items():
            if f==0:continue
            result.append(c*f)# add extra chars that arent part of order
        del order, string_count
        return "".join(result)

"""
Solution 2: Just sort the string based on order of chars indexes in priority dict

Runtime 28 ms Beats 98.59%
Memory 16.2 MB Beats 94.16%

TC: O(nlogn+o(m))  where m=len(order), n = len(string)
SC: O(m) for priority dict
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        priority = collections.defaultdict(int)
        for i, c in enumerate(order): priority[c]=i
        return "".join(sorted(s, key=lambda c : priority[c]))