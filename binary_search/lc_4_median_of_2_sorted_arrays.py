# https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
Brute force solution
Success
Details 
Runtime: 91 ms, faster than 97.54% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 67.12% of Python3 online submissions for Median of Two Sorted Arrays.
TC: O((m+n)log(m+n))
SC:O(m+n)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=sorted(nums1+nums2)
        mid=0+(len(merged)-1)//2
        return merged[mid] if len(merged)%2!=0 else (merged[mid]+merged[mid+1])/2