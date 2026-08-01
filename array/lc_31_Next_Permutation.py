# https://leetcode.com/problems/next-permutation/description/
"""
Solution
TC:O(n)
SC:O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find Pivot i where nums[i] < nums[i+1]
        # 2. find no on right of pivot i which is just greater than pivot
        # 3. swap pivot and this larger no
        # 3. reverse rest of the string on right
        n = len(nums)
        if len(nums) < 2: return
    
        def reverse_list(start_idx, end_idx):
            while start_idx < end_idx:
                nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                start_idx += 1
                end_idx -= 1
            return
        # find the pivot where nums[i] < nums[i+1]
        pivot_idx = n-1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot_idx = i
                break
        if pivot_idx == n - 1:
            reverse_list(start_idx=0, end_idx=n-1)
            return
        # find number larger just than pivot
        swap_idx = n-1
        while swap_idx > pivot_idx:
            if nums[swap_idx] > nums[pivot_idx]:
                break
            swap_idx -= 1
        # swap
        nums[pivot_idx], nums[swap_idx] = nums[swap_idx], nums[pivot_idx]
        # reverse list to next lexi larger no
        reverse_list(start_idx=pivot_idx+1, end_idx=n-1)
        return
