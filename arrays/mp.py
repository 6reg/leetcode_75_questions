def maxProfit(nums):
    max_profit, min_price=0, float('inf')
    for num in nums:
        min_price=min(min_price, num)
        profit=price-min_price
        max_profit=max(max_profit,profit)
        return max_profit
print(maxProfit([1,4,5,8]))
