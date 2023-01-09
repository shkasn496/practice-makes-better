# https://leetcode.com/problems/decode-string/description/
"""
Solution:
Runtime 27 ms Beats 95.1%
Memory 13.8 MB Beats 98.59%

TC: O(maxK*n)
SC:O(maxK*n)
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack, num=[],0
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c != ']':
                if num>0:stack.append(num)
                stack.append(c)
                num=0
            else:
                temp=""
                while stack[-1]!='[':
                    temp=stack.pop()+temp
                stack.pop() #remove [
                stack.append(temp*stack.pop())
                del temp
        return "".join(stack)