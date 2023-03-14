# https://leetcode.com/problems/random-pick-with-weight/description/
"""
Solution
Runtime 221 ms Beats 88.13%
Memory 18.4 MB Beats 94.76%

TC: O(n) init
    O(logN) pickIndex
SC: O(n) init
    O(1) pickIndex
"""
class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = []
        self.total=0
        for e in w:
            self.total+=e
            self.cum_sum.append(self.total)
        return

    def pickIndex(self) -> int:
        idx = random.uniform(0,self.total)
        l, r = 0, len(self.cum_sum)
        while l < r:
            mid = l+(r-l)//2
            if idx>self.cum_sum[mid]:l=mid+1
            else:r=mid
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

"""
Solution 2: Will give TLE but is simpler to understand

"""
class Solution:

    def __init__(self, w: List[int]):
        self.weights=[]
        for i,_w in enumerate(w):
            for _ in range(_w):
                self.weights.append(i)
        return

    def pickIndex(self) -> int:
        random_idx = random.uniform(0,len(self.weights))
        return self.weights[random_idx]