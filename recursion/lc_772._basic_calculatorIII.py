# https://leetcode.com/problems/basic-calculator-iii/description/
"""
Solution 1: Recursion Helper + Stack
Runtime 33 ms Beats 94.19%
Memory 13.9 MB Beats 90.57%
TC: O(n)
SC: O(n)+O(n) recursive stack
"""
class Solution:
    def calculate(self, s: str) -> int:
        def calc_recurse(idx):
            num, sign, stack = 0,'+',[]
            def update_operation(num,sign):
                if sign=='+':stack.append(num)
                elif sign=='-':stack.append(-num)
                elif sign=='*':stack.append(stack.pop()*num)
                else:stack.append(int(stack.pop()/num))
                return
            while idx < len(s):
                c=s[idx]
                if c.isdigit():
                    num=num*10+int(c)                    
                elif c in '+-*/':
                    update_operation(num, sign)
                    num,sign = 0, c
                elif c=='(':
                    num, idx = calc_recurse(idx+1)
                elif c==')':
                    update_operation(num, sign)
                    return sum(stack), idx
                idx+=1
            update_operation(num, sign)
            return sum(stack)
        return calc_recurse(0)