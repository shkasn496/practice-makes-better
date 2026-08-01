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
        if len(nums)==1: return 1
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] <= nums[slow]: # encountered a duplicate
                fast += 1
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
        return slow+1

"""
Solution 2: Better solution
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        slow = 1
        for fast in range(1, len(nums)):
            if nums[slow - 1] != nums[fast]:
                nums[slow] = nums[fast] # override no at slow pointer
                slow += 1
        return slow