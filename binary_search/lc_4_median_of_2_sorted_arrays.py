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

"""
Optimized solution : Binary Search solution on smaller array & no sorting

Runtime 84 ms Beats 99.11%
Memory 14.2 MB Beats 24.12%

TC: O(log(min(m,n)))
SC: O(1)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):return self.findMedianSortedArrays(nums2, nums1)
        total=len(nums1)+len(nums2)
        half=total//2
        l, r=0, len(nums1)-1
        while True:
            partition1=l+(r-l)//2 # left partition elements in smaller array
            partition2=half-(partition1+1)-1 # left partition elements in larger array

            l1 = nums1[partition1] if partition1 >=0 else -float("inf")
            r1 = nums1[partition1+1] if partition1+1 <len(nums1) else float("inf")

            l2 = nums2[partition2] if partition2 >=0 else -float("inf")
            r2 = nums2[partition2+1] if partition2+1 <len(nums2) else float("inf")
            #found the correct partition
            if l1 <=r2 and l2 <=r1:
                if total % 2==0:return (max(l1, l2)+min(r1, r2))/2
                return min(r1,r2)
            elif l1 > r2:r=partition1-1 # move left boundary partition one step to the left
            elif l2 > r1:l=partition1+1 # move left boundary partition one step to the right
        return -1