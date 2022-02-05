def two_sum nums, target
  hm = Hash.new
  nums.each.with_index do |num, index|
    diff = hm[target - num]
  return [diff, index] if diff 
  hm[num] = index
  end
end

puts two_sum [1,2,4,5,5], 10

