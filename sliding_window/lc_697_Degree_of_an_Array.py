# https://leetcode.com/problems/degree-of-an-array/description/
"""
Solution 1: Store the degrees of numbers in a dict.
            Store the starting index of num in start dict.
            Store ending occurence index num in end dict.
            Traverse the nums that have max degree and check which sliding 
            window has smallest length. (end_idx - start_idx + 1)

Runtime 187 ms Beats 97.40%
Memory 17.8 MB Beats 72.90%

TC: O(n)
SC:O(n)
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree, start, end = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in degree:
                degree[num]=1
                start[num]=i
                end[num]=i
            else:
                degree[num]+=1
                end[num]=i
        max_degree = max(degree.values())
        min_contiguous_len = len(nums)
        for num, deg in degree.items():
            if deg==max_degree:
                min_contiguous_len = min(min_contiguous_len, \
                                        end[num]-start[num]+1)
        del degree, start, end
        return min_contiguous_len