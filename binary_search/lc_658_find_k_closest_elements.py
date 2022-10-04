# https://leetcode.com/problems/find-k-closest-elements/
"""
Success
Details 
Runtime: 359 ms, faster than 82.81% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.5 MB, less than 80.94% of Python3 online submissions for Find K Closest Elements.
TC: O(n+log(k))+klogk SC:O(k)
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

"""
Better solution: Find closest idx first, then do k iterations
Success
Details 
Runtime: 301 ms, faster than 96.06% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.6 MB, less than 46.43% of Python3 online submissions for Find K Closest Elements.
TC: O(logn+k)
SC:O(1)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N=len(arr)
        def get_closest_number_to_x():
            l, r = 0, N-1
            while l<r-1:
                m=l+(r-l)//2
                if arr[m]==x:return m
                elif arr[m]>x:r=m
                else:l=m
            dist_l, dist_r=abs(arr[l]-x),abs(arr[r]-x)
            return l if dist_l<=dist_r else r
        
        target_idx= get_closest_number_to_x()
        #initialized pointers to target idx
        left_idx=right_idx=target_idx
        
        while right_idx-left_idx+1<k: #iterate loop while pointers don't match k
            new_left, new_right=left_idx-1, right_idx+1
            if new_left>=0 and new_right<N:
                dist_l, dist_r=abs(arr[new_left]-x),abs(arr[new_right]-x)
                if dist_l<=dist_r:left_idx-=1
                else:right_idx+=1
            elif new_left<0 and new_right<N:right_idx+=1
            else:left_idx-=1
        return arr[left_idx:right_idx+1]

"""
Best solution: Just start with two pointers at ends of list and reduce to k
Success
Details 
Runtime: 281 ms, faster than 99.47% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.4 MB, less than 81.61% of Python3 online submissions for Find K Closest Elements.
TC: O(n-k)
SC:O(1)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right= 0, len(arr)-1
        while right -left+1>k:
            if abs(arr[left]-x)<=abs(arr[right]-x):right-=1
            else:left+=1
        return arr[left:right+1]

# Case 1: when large N, small K
# Solution 2 will work best  TC: O(log(N)+k) ~= O(logN)
# Solution 3 wont work as good for this case TC: O(N-k) ~= O(N)

# Case 2: When large N, large K
# Solution 2 wont work as good for this case  TC: O(log(N)+k) ~= O(logN+log(N)) ~= O(logN)
# Solution 3 will work best TC: O(N-k) ~= O(N-N) ~= O(1)