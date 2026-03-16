# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
"""
Solution
TC: O(n)
SC: O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) <= 2: return len(nums)
        max_length = curr_k = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr_k += 1
            while curr_k > k:
                if nums[left] == 0:
                    curr_k -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length