# https://leetcode.com/problems/meeting-scheduler/description/
"""
Solution 1: Using 2 Pointers for traversing the slots
Runtime 532 ms Beats 97.6%
Memory 21.5 MB Beats 77.8%

TC: O(MlogM + NlogN) M=len(slots1), N=len(slots2)
SC: O(M+ N) M=len(slots1), N=len(slots2) for sorting
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        i= j = 0
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            s, e = max(s1, s2), min(e1, e2)
            if e-s>=duration:return [s,s+duration]
            elif e==e2:j+=1
            elif e==e1:i+=1
        return []