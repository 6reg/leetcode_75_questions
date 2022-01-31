def hm(nums, targ)
  my_hm = Hash.new
  nums.each.with_index do |num, i|
    diff = my_hm[targ - num]
    return [diff, i] if diff != nil
  my_hm[num] = i
  end
end

puts hm([3,4,5,6], 11)
