"""
This program takes a list of numbers, finds the greatest number and the least number and returns the difference.
"""

def mp(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

print(mp([1, 5, 2, 56, 2, 100]))
