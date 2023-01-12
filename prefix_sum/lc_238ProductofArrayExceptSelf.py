# https://leetcode.com/problems/product-of-array-except-self/description/
"""
Solution : Optimized solution
Runtime 222 ms Beats 98.21%
Memory 21.2 MB Beats 75.70%
TC: O(n)
SC: O(1)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, postfix = len(nums), 1
        products = [1]*n
        # calculate prefix products of elements
        for i in range(1, n):
            products[i]=products[i-1]*nums[i-1]
        #calculate postfix products of elements
        for i in range(len(nums)-1, -1, -1):
            products[i]*=postfix
            postfix*=nums[i]
        return products