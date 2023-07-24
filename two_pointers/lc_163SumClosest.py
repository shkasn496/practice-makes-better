# https://leetcode.com/problems/3sum-closest/description/
"""
Solution 1: Two pointers
Runtime 1042 ms Beats 75.30%
Memory 13.9 MB Beats 94.44%
TC: O(n^2+nlogn)
SC:O(n)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum=sum(nums[:3])
        nums.sort()
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                temp_sum = nums[i]+nums[start]+nums[end]
                if abs(target-temp_sum)<abs(target-closest_sum):closest_sum=temp_sum
                if temp_sum <target:start+=1
                else:end-=1
        return closest_sum