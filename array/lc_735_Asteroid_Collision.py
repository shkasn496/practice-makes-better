# https://leetcode.com/problems/asteroid-collision/description/
"""
Runtime 99 ms Beats 94.67%
Memory 15.2 MB Beats 73.11%

TC: O(n)
SC : O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            while stack and a < 0 < stack[-1]: # asteroidCollision
                if abs(a)> abs(stack[-1]):
                    stack.pop()
                elif abs(a) < abs(stack[-1]):
                    a=0
                else:
                    a=0
                    stack.pop()
            if a !=0:
                stack.append(a)
        return stack