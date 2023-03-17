# https://leetcode.com/problems/move-zeroes/description/
"""
Solution 1: Twoo pointers, cleaner code
Runtime 155 ms Beats 98.19%
Memory 15.7 MB Beats 10.15%
TC:O(n)
SC:O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:return
        slow=0
        for fast in range(1, len(nums)):
            if not nums[slow] and nums[fast]:#swap
                nums[slow],nums[fast]=nums[fast],nums[slow]
            if nums[slow]:slow+=1
        return

"""
Solution 2: Same technique, but not so clean code
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:return
        i, j = 0,1
        while j<len(nums):
            if not nums[i] and nums[j]:#swap
                nums[i],nums[j]=nums[j],nums[i]
            elif not nums[i] and not nums[j]:
                j+=1
            else:
                i+=1
                j+=1
        return