# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
Solution 1: Optimized DP Tabulation (Kadane's algo)

TC: O(n)
SC: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        buy = prices[0]
        max_profit = 0
        for sell in prices[1:]:
            if sell < buy:
                buy = sell
            else:
                max_profit = max(max_profit, sell - buy)
        return max_profit