# https://leetcode.com/problems/product-of-array-except-self/description/
"""
Solution : Calculate prefix product  of all elements first.
            Instead of storing another array to store suffix products and then multiply the two arrays,
            I simply store the current suffix in a variable and update it with the nums array.

Runtime 175 ms Beats 99.55%
Memory 24.1 MB Beats 57.4%

TC: O(n)
SC: O(1)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, suffix = len(nums), 1
        prefix = [1]*n
        # calculate prefix products of elements
        for i in range(1, n):
            prefix[i]=prefix[i-1]*nums[i-1]
        #calculate suffix products of elements
        for i in range(len(nums)-1, -1, -1):
            prefix[i]*=suffix
            suffix*=nums[i]
        return prefix