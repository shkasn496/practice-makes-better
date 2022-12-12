# https://leetcode.com/problems/two-sum-less-than-k/description/

"""
Solution 1: brute forcs

TC: O(n^2)
SC: O(1)
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums)< 2:return -1
        maxSum = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sumV = nums[i] + nums[j]
                if sumV >=k:continue
                maxSum = max(maxSum, sumV)
        return maxSum

"""
Solution 2: Sort, then traverse from front and back

Runtime 36 ms Beats 99.25%
Memory 13.9 MB Beats 23.62%

TC : O(n*logN)
SC: O(1)
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:return -1
        nums.sort()
        s, e = 0, len(nums)-1
        maxSum = -1
        while s!=e:
            sum = nums[s]+nums[e]
            if sum >=k:
                e-=1
            else:
                maxSum = max(maxSum, sum)
                s+=1
        return maxSum

