# https://leetcode.com/problems/find-k-closest-elements/
"""
Success
Details 
Runtime: 359 ms, faster than 82.81% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.5 MB, less than 80.94% of Python3 online submissions for Find K Closest Elements.
TC: O(n*log(k)) SC:O(k)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:return arr[:k]
        if x>=arr[-1]:return arr[len(arr)-k:]
        closeValue = [0, abs(arr[0]-x)]
        for i in range(1,len(arr)):
            if abs(arr[i]-x)<closeValue[1]: closeValue= [i, abs(arr[i]-x)]
        # can also do binary search to find closest value to target
        indices=[arr[closeValue[0]]]
        left,right=closeValue[0]-1,closeValue[0]+1
        while len(indices)<k :
            leftdist=rightdist=-1
            if 0<=left<len(arr):leftdist=abs(arr[left]-x)
            if 0<=right<len(arr):rightdist=abs(arr[right]-x) 
            if leftdist!=-1 and rightdist!=-1:
                if leftdist<=rightdist:
                    indices.append(arr[left])
                    left-=1
                else:
                    indices.append(arr[right])
                    right+=1
            else:
                if leftdist!=-1 and rightdist==-1:
                    indices.append(arr[left])
                    left-=1
                else:
                    indices.append(arr[right])
                    right+=1
        return sorted(indices)  