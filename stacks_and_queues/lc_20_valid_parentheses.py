# https://leetcode.com/problems/valid-parentheses/description/
"""
Solution: Using stack and hashmap for bracket relationship
Runtime 23 ms Beats 98.4%
Memory 13.9 MB Beats 61.35%
TC: O(n)
SC: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in ")]}" or len(s)% 2 != 0 : return False
        stack=[]
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c not in mapping: # open bracket
                stack.append(c)
            else: # close bracket
                if not stack or (stack and stack.pop() != mapping[c]):
                    return False
        stack_len = len(stack)
        del mapping, stack
        return stack_len==0

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 : return False
        mapping = {")":"(", "}":"{", "]":"["}
        stack = []
        flag = False
        for c in s:
            if c not in mapping.keys(): # open bracket
                stack.append(c)
            else: # close bracket
                if not stack or mapping[c] != stack.pop():
                    flag = True
            if flag: break
        flag = flag | len(stack)>0
        del stack, mapping
        return not flag
