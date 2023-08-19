# https://leetcode.com/problems/subarray-product-less-than-k/description/

"""
Solution 1: Brute Force. Works but give Time Limit Exceeded.
TC: O(n^2)
SC:O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        if k<=1:return result
        for i in range(len(nums)):
            if nums[i]>=k:continue
            result+=1
            product=nums[i]
            for j in range(i+1, len(nums)):
                if product*nums[j]>=k:break
                product*=nums[j]
                result+=1
        return result

"""
Solution 2: Sliding Window
            ans += right - left + 1 in "Sliding Window" approach. 
            Because the element pointed by the "right" is the new one 
            we are investigating, as long as we find a subarray with 
            prod < k after being divided by nums[left], ans should be 
            increased by the length of the subarray because the product 
            is ever increasing. For example, [10,5,2,6], when right 
            points to 6, left points to 5, ans added 3, which is due 
            to [5,2,6],[2.6],and[6].

Runtime 651 ms Beats 99.9%
Memory 19.3 MB Beats 96.63%
TC:O(n)
SC:O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        if k<=1:return result
        left, product = 0, 1
        for right, val in enumerate(nums):
            product*=val
            while product >= k:
                product /= nums[left] # divide left pointer element
                left+=1
            result += right - left + 1 #sliding window
        return result