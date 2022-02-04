def two_sum(nums, target)
  hm = Hash.new
  nums.each.with_index do |num, index|
    diff = hm[target - num]
    return [diff, index] if diff != nil
  hm[num] = index
  end
end

puts two_sum([1,2,3,4,5], 9)
