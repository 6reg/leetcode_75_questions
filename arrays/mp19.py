def mp(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit

print(mp([20, 4, 5, 5, 23, 4]))
