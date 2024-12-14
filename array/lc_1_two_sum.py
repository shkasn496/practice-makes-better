# https://leetcode.com/problems/two-sum/description/

"""
Solution 1: Brute Force
Runtime 1209 ms Beats 26.75%
Memory 14.9 MB Beats 96.9%
TC: O(n^2)
SC: O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                nums1, nums2 = nums[i], nums[j]
                if nums1 + nums2 == target:
                    return [i,j]

"""
Solution 2: Optimized solution, going through array only once
Runtime 0 ms Beats 100%
Memory 18.32 MB Beats 14.94%

TC : O(N)
SC : O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        mapping = {}
        answer = []
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in mapping:
                answer = [i, mapping[num2]]
                break
            mapping[num1] = i
        del mapping
        return answer