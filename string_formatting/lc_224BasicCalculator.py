# https://leetcode.com/problems/basic-calculator/description/
"""
Runtime 62 ms Beats 99.63%
Memory 15.4 MB Beats 47.88%

TC: O(n)
SC: O(n)
"""
class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==1:return int(s)
        result=0
        sign = 1 # if '+' else -1 if '-'
        operand=0
        stack=[]
        for c in s:
            if c is ' ':continue
            if c.isdigit():
                operand=operand*10 + int(c)
            elif c in {'+', '-'}:
                # multiply previous sign and operand info to result
                result+= sign * operand
                # reset sign and operand
                operand=0
                sign = 1 if c is "+" else -1
            elif c is '(':
                stack.append(result)
                stack.append(sign)
                # reset result and sign to compute result in brackets
                result, sign = 0, 1
            elif c is ')':
                # multiply previous sign and operand info to result
                result+= sign * operand
                # multiply stack sign with current result
                result*=stack.pop()
                # now add previously stored result from the stack
                result+=stack.pop()
                operand=0
        del stack
        return result+sign*operand