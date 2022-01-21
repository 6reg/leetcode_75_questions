def two_sum(nums, target)
  hm = Hash.new
  nums.each_with_index do |element, index|
    diff = hm[target - element]
    return [diff, index] if diff != nil
    hm[element] = index
  end
end

puts two_sum([1,2,3,4], 7)

