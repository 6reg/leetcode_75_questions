class Solution:
    def maxProfit(self, prices): # define class maxProfit
        maxProfit = 0 # create var to store result
        minPurchase = prices[0] # create var to store smallest int
        for i in range(1, len(prices)): # loop through each index in prices
            maxProfit = max(maxProfit, prices[i] - minPurchase) # assign maxProfit var to greater of current maxProfit or current prices int minus current minPurchase int
            minPurchase = min(minPurchase, prices[i]) # assign lesser of current minPurchase / current prices int
        return maxProfit

mp = Solution()
print(mp.maxProfit([1,5,6,9]))
