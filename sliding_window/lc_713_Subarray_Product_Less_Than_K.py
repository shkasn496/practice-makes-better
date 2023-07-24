# https://leetcode.com/problems/subarray-product-less-than-k/description/

"""
Solution 1: Brute Force. Works but give Time Limit Exceeded.
TC: O(n!)
SC:O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:return k
        if len(nums)==1:return nums[0] if nums[0]<k else 0
        sub_array_count=0
        for i in range(len(nums)):
            if nums[i]>=k:continue
            prod=1
            for n in nums[i:len(nums)]:
                prod *= n
                if prod<k: sub_array_count+=1
                else: break
        return sub_array_count

"""
Solution 2: Sliding Window
Runtime 651 ms Beats 99.9%
Memory 19.3 MB Beats 96.63%
TC:O(n)
SC:O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:return 0
        ans = left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product//= nums[left]
                left += 1
            ans += right-left+1
        return ans