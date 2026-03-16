# https://leetcode.com/problems/move-zeroes/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

"""
Solution : Two pointers
TC: O(n)
SC: O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1: return
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != 0: # find the first zero elem
                i += 1
                j += 1
            else:
                # find the first non-zero elem to swap values with 0
                while j < len(nums) and nums[j]==0:
                    j += 1
                if j >= len(nums): break
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return
