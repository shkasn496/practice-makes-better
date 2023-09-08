# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

"""
Solution 1: Use two pointer, slow and fast.
            Maintain a counter duplicates.
            If nums[fast] != last_found:
                copy data from fast pointer into slow pointer location,
                update slow pointer and reset duplicate count
            If nums[fast] == last_found:
                if duplicate count is less than 1:
                    copy data from fast pointer into slow pointer location,
                    update slow pointer and update duplicate count

Runtime 49 ms Beats 96.1%
Memory 16.4 MB Beats 51.14%

TC: O(n)
SC :O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        slow, fast, n = 0, 0, len(nums)
        last_found = -10**4 - 1
        duplicates = 0
        while fast < n:
            if nums[fast] != last_found:
                nums[slow] = last_found = nums[fast]
                slow += 1
                duplicates = 0
            else:
                if duplicates < 1:
                    nums[slow] = nums[fast]
                    slow += 1
                    duplicates += 1
            fast += 1
        return slow