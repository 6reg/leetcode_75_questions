def maxProfit(prices):
    max_profit, min_price= 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit([1, 3, 5, 8]))
