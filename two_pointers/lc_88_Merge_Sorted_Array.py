# https://leetcode.com/problems/merge-sorted-array/description/
"""
Solution 1: Using 3 pointers and no memory
Runtime 31 ms Beats 99.73%
Memory 16.2 MB Beats 84.46%
TC:O(m+n)
SC:O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i] <= nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1
        return
    
"""
Solution 2: No while loops
Runtime 0 ms Beats 100.00%
Memory 17.23 MB Beats 20.00%

TC:O(m+n)
SC: O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 or n==0:
            if m==0: nums1[:n]=nums2
            return
        i, j = m-1, n-1
        for k in range(m+n-1,-1,-1):
            if i==-1 or j==-1:break
            if nums1[i] <= nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
        if j>=0:nums1[:j+1]=nums2[:j+1]
        return