# https://leetcode.com/problems/sort-characters-by-frequency/description/
"""
Solution 1: Store the frequency of counts and add them to result in reverse order
Runtime 48 ms Beats 77.81%
Memory 17.6 MB Beats 60.65%
TC: O(n) + O(klogk) where k=longest set containing same freq elements
SC:O(n)
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        letters = collections.Counter(s)
        counts = collections.defaultdict(set)
        for c, val in letters.items():
            counts[val].add(c)
        del letters
        max_count = max(counts.keys())
        result=[]
        for val in range(max_count,0, -1):
            if val not in counts:continue
            for c in sorted(counts[val]):
                result.append(c*val)
        del counts
        return "".join(result)

"""
Solution 2: Sort the dict by values and add to result
Runtime 27 ms Beats 99.77%
Memory 17.7 MB Beats 27.98%
TC:O(nlogn)
SC:O(n)
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        result=[]
        for c, f in sorted(freq.items(), key=lambda elem:elem[1], reverse=True):
            result.append(c*f)
        del freq
        return "".join(result)