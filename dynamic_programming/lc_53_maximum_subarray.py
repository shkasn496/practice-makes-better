# https://leetcode.com/problems/maximum-subarray/description/

"""
Solution 1: DP Tabulation method

TC: O(n)
SC: O(n)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        subarray_sum = [0] * N
        subarray_sum[0] = nums[0]
        for i in range(1, N):
            subarray_sum[i] = nums[i] + max(0, subarray_sum[i-1]) #either extend subarray OR start new one
        return max(subarray_sum)

"""
Solution 2: Memory optimized Tabulation method

TC: O(n)
SC: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        prev_sum = max_sum = nums[0]
        for i in range(1, N):
            curr_sum = nums[i] + max(0, prev_sum) #either extend subarray OR start new one
            prev_sum = curr_sum
            max_sum = max(prev_sum, max_sum)
        return max_sum
    
"""
Solution 3: Kadane's algorithm

TC: O(n)
SC: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum