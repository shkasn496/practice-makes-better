# https://leetcode.com/problems/binary-search/description/
"""
Solution 1: Binary search template with overflow handling

Runtime 0ms Beats 100.00%
Memory 18.82MB Beats 27.44%

TC: O(logN)
SC: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1
        l, r = 0, len(nums) - 1
        while l < r :
            mid = l + (r - l)//2
            if nums[mid] == target: return mid
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1