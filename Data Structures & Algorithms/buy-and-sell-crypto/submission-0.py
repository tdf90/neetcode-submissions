class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            # profit is only minus the current (lowest)
            # buy price we've seen, since its a lookback
            profit = max(price-buy_price, profit)

            # lower the buy price if we can
            buy_price = min(price, buy_price)

        return profit