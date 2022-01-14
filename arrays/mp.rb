def max_profit(prices)
  return 0 if prices.count < 2

  differences = (1..prices.count-1).reduce([]) {|ar, i| ar << (prices[i] - prices[i-1])}
  maximum_subarray_sum(differences)
end

# Kandane's Algorithm
def maximum_subarray_sum(array)
  max_ending_here, max_so_far = 0, 0

  array.each do |ele|
    max_ending_here = [ 0, max_ending_here + ele ].max
    max_so_far = [ max_so_far, max_ending_here  ].max
  end

  max_so_far
end

puts max_profit([3, 5, 6, 6])
