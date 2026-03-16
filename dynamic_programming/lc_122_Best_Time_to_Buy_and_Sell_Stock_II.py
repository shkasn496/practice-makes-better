# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""
Solution : Calculate the times that sell price is greater than buy price and sum it
        since we can buy and hold only one share at a time
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        max_profit = 0
        for buy, sell in zip(prices, prices[1:]):
            if sell > buy:
                max_profit += sell - buy
        return max_profit