def max_profit(prices):
    min_price, max_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_price = max(max_price, price)
        profit = max_price - min_price
    return profit

print(max_profit([1,5,5,8]))
