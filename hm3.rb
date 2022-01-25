def two_sum(nums, target)
  hm = Hash.new
  nums.each_with_index do |value, index|
    diff = hm[target - value]
    return [diff, index] if diff != nil
    hm[value] = index
  end
end

puts "#{two_sum([2,4,5,6], 11)}"
