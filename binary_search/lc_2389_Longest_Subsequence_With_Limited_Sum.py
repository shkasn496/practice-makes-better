# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
"""
Runtime 15 ms Beats 66.55%
Memory 18.06 MB Beats 5.67%

TC: O(nlogn)+ O(n) + o(mlogm)
SC: O(n)
"""
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort() # O(nlogn)
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)): # O(n)
            prefix_sum.append(prefix_sum[i-1]+nums[i])
        answer=[0]*len(queries)
        for i, q in enumerate(queries): # O(m)
            answer[i]=self.binarySearch(prefix_sum, q) # O(logm)
        del prefix_sum
        return answer

    def binarySearch(self, arr, target):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid]<=target:low=mid+1
            else: high=mid-1
        return low