# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
"""
Very useful doc: 
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/solutions/777019/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/

TC: O(NlogM) where N -> length of nums, M is max element in nums
SC: O(1)
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) == threshold: return max(nums)
        def condition(divisor) -> bool:
            return sum(ceil(n/mid) for n in nums) <= threshold
        low, high = 1, max(nums)
        while low < high:
            mid = low + (high - low)//2
            if condition(mid): high = mid
            else: low = mid + 1
        return low