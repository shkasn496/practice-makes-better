# https://leetcode.com/problems/group-shifted-strings/description/
"""
Solution 1: Store the shifting of strings as hashkey/pattern
Runtime 42 ms Beats 59%
Memory 16.3 MB Beats 38.40%
TC: O(n*k) where k=max(len(string))
SC: O(n)
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts_and_strings=collections.defaultdict(list)
        for string in strings:
            shift=[]
            for i in range(len(string)-1):
                diff = ord(string[i+1])-ord(string[i])
                if diff < 0:diff+=26 #handle corner case "az"->"ba"
                shift.append(diff)
            shifts_and_strings[tuple(shift)].append(string)
        return shifts_and_strings.values()