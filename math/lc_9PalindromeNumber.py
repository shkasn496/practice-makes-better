# https://leetcode.com/problems/palindrome-number/description/
"""
Solution1: Reverse string
Runtime 49 ms Beats 98.62%
Memory 13.8 MB Beats 97.3%

TC:O(n)
SC:O(n)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        num=int(str(x)[::-1])
        return num==x

"""
Solution 2 on Follow Q: Follow up: Could you solve it without converting the integer to a string?
Take mod of num and keep dividing number

Runtime 59 ms Beats 92.79%
Memory 13.8 MB Beats 97.3%

TC:O(n)
SC:O(1)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        num_og, num_r = x, 0
        while x:
            num_r=num_r*10+x%10
            x//=10
        return num_r==num_og

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        if x < 10: return True
        if x % 10==0: return False
        temp = x
        reversed_no = 0
        while temp:
            digit = temp % 10
            reversed_no = reversed_no * 10 + digit
            temp = temp // 10
        return x == reversed_no
        