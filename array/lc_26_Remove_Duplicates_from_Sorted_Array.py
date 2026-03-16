# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
"""
Solution 1: 

TC: O(n)
SC: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2 : return len(nums)
        i, j = 0, 1 # correct, incorrect pointers
        while j < len(nums):
            if nums[i] == nums[j]: # duplicate
                j += 1
            else:
                # found unique number in j position
                nums[i+1], nums[j] = nums[j], nums[i+1] # swap
                i += 1
                j += 1
        return i + 1