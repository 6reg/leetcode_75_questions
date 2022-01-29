def two_sum(nums, target)
  hm = Hash.new
  nums.each_with_index do |item, index|
    diff = hm[target-item]
    return [diff, item] if diff != nil
    hm[item] = index
  end
end

puts two_sum([3,3,4,5,], 9)
