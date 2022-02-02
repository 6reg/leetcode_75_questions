def two_sum(nums, target)
  hm = Hash.new
  nums.each_with_index do |num, i|
    diff = hm[target - num]
    return [hm[diff], i] if hm[diff] != nil
  hm[i] = num
  end
end

puts two_sum([1,2,3,4,5], 9)
