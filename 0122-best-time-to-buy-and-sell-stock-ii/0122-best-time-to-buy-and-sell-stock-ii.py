class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mua vào ngày ít nhất và bán vào ngày nhiều nhất
        max_profit = 0
        for price in range(1, len(prices)):
            max_profit += max(0, prices[price] - prices[price - 1])
        return max_profit