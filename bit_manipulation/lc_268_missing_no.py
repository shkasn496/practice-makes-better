# https://leetcode.com/problems/missing-number/
"""
Success
Details 
Runtime: 127 ms, faster than 99.43% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 41.93% of Python3 online submissions for Missing Number.
TC : O(n)
SC : O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return int((n*(n+1)/2)-sum(nums)) #gaussian formula

class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        # XOR of Indexes
        for i in range(0, len(nums) + 1): xor ^= i
        # XOR of Numbers
        for num in nums: xor ^= num
        # Finally, xor will be equal to the missing number
        return xor