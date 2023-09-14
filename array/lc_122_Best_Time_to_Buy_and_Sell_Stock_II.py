# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""
Solution 1: Calculate positive price differences
Runtime 55 ms Beats 95.96%
Memory 17.6 MB Beats 91.43%
TC:O(N)
SC:O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0: max_profit += profit
        return max_profit