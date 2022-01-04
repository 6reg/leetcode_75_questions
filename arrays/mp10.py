def mp(prices):
    low = 0
    for i in range(1, len(prices)):
        high = i
        mp = high - low
