def main
  def max_profit(prices)
    return 0 if prices.count < 2

    profit = 0
    min_price = prices[0]

    (1..prices.count-1).each do |k|
      # profit represents max profit from day 0 to day k
      # min_price represents minimum prices from day 0 to day k-1
      profit = prices[k] - min_price if profit < prices[k] - min_price
      min_price = prices[k] if prices[k] < min_price
    end

    profit
  end
  puts max_profit([7,1,5])
end
if __FILE__ == $0
  main
end
