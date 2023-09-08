# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
Solution 1: Use two pointers, a fast and slow pointer.
            The fast pointer gets updated every iteration
            The slow pointer keeps track of all unique elements 
                and updates the last found elem and itself when nums[fast] != last_found
            Return slow pointer as 'k'.

Runtime 74 ms Beats 97.35%
Memory 17.9 MB Beats 50.55%

TC:O(n)
SC:O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:return len(nums)
        i, j, n = 0, 0, len(nums)
        last_found = -101
        while j < n:
            if nums[j] != last_found:
                nums[i] = last_found = nums[j]
                i+=1
            j+=1
        return i