# https://leetcode.com/problems/top-k-frequent-elements/description/
"""
Solution 1: Optimized to run in O(n)
Runtime 135 ms Beats 80.70%
Memory 31.5 MB Beats 6.3%

TC: O(n)
SC:O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1 and k==1:return nums
        result=[]
        # key: count of occurrences, val: set of nums elements that map to occurrence
        occurrences= {i: set() for i in range(1,len(nums)+1)}
        nums_freq = {elem: 0 for elem in nums}
        # fill occurrences
        for elem in nums: nums_freq[elem]+=1
        for elem in nums:
            count = nums_freq[elem]
            occurrences[count].add(elem)
        del nums_freq
        # traverse count in reverse order to get max frequency elements
        for count in reversed(occurrences.keys()):
            if len(result)==k:break
            elems=occurrences[count]
            if len(elems)<1:continue
            for i in elems:
                result.append(i)
                if len(result)==k:break
        del occurrences
        return result