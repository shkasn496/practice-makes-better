# https://leetcode.com/problems/plus-one/
"""
Solution 1: Add the digits to form the number, then increment by 1 and return the number
Runtime 44 ms Beats 79.79%
Memory 13.8 MB Beats 96.76%

TC: O(n)
SC: O(n)
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no , pow=0,len(digits)-1
        for digit in digits:
            no+= digit* 10 ** pow
            pow-=1
        return [int(i) for i in str(no+1)]

"""
Solution 2: Increment the digits starting from LSB to MSB. Could be helpful for larger numbers
Runtime 29 ms Beats 98.10%
Memory 24 MB Beats 11.85%
TC: O(n)
SC: O(n)
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:return digits
        if digits[-1]<9:
            digits[-1]+=1
            return digits 
        carry=1 #added plus one
        output=[0] #remainder is 0
        for i in range(len(digits)-2, -1, -1):
            d = digits[i]
            if carry:
                elem = d+carry
                carry = 0 if elem <= 9 else 1
                if carry:elem = 0
                output.append(elem)
            else:output.append(d)
        if carry:output.append(carry)
        return reversed(output)