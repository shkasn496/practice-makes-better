# https://leetcode.com/problems/random-pick-with-weight/description

"""
Solution
"""
class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.cum_sum = [0] * self.n
        self.cum_sum[0] = w[0]
        for i in range(1, self.n):
            self.cum_sum[i] = self.cum_sum[i-1] + w[i]
        self.total = self.cum_sum[-1]


    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, r = 0, self.n - 1
        while l < r:
            mid = l + (r-l)//2
            if self.cum_sum[mid] == target:
                return mid
            elif self.cum_sum[mid] > target:
                r = mid
            else:
                l = mid+1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()