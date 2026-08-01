# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
Solution 1: Two pointers
TC: O(n)
SC: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
        return []