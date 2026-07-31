class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # Best profit if we sell today.
            max_profit = max(max_profit, price - buy_price)

            # Cheapest buying price seen so far.
            buy_price = min(buy_price, price)

        return max_profit