def two_sums(nums, target)
  hm = Hash.new
  nums.each_with_index do |num, index|
    diff = hm[target - num]
    return [diff, index] if diff != nil
    hm[num] = index
  end
end

puts two_sums([3,5,6,4,3], 11)
