# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
"""
Solution 1: Optimized solution no extra space
Runtime 73 ms Beats 59.11%
Memory 16.9 MB Beats 48%
TC:O(n)
SC:O(1)
"""
class Solution:
    def numSub(self, s: str) -> int:
        ones_count, i, N = 0, 0, len(s)
        while i < N:
            if s[i]=='0':i+=1
            else:
                j=i
                while j<N and s[j]=='1':j+=1
                one_occurs = j-i # eg: 5 ones = 5+4+3+2+1 patterns found
                #n(n+1)/2 to get sum of values
                ones_count+=one_occurs*(one_occurs+1)//2
                i=j+1
        return ones_count%(10**9 + 7)

"""
Solution 2: Split the string where there are zeros. Now each elem contains
            length of 1's.
            This solution is slightly faster although it uses memory.
Runtime 42 ms Beats 97.79%
Memory 17.5 MB Beats 18.14%
TC:O(n)
SC:O(n)
"""
class Solution:
    def numSub(self, s: str) -> int:
        s=s.split('0')
        ones_count, N = 0, len(s)
        for i in range(N):
            n=len(s[i])
            ones_count+=n*(n+1)//2
        del s
        return ones_count%(10**9 + 7)