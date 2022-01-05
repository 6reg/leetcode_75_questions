def maxProfit(prices):
    max_profit, min_price = 0, float('inf') # declare variables and assign vals
    for price in prices: # loop through prices list
        min_price = min(min_price, price) # assign either float('inf') or prices[0] to min_price
        profit = price - min_price # if prices = [1,3,5,2], profit = 1
        max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit([1,3,5,2]))
