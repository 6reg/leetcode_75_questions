def maxProfit(prices):
    maxProfit = 0
    minPurchase = prices[0]
    for i in range(1, len(prices)):
        maxProfit = max(maxProfit, prices[i] - minPurchase)
        minPurchase = min(minPurchase, prices[i])
    return maxProfit

print(maxProfit([1,3,5]))
