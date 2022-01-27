def two_sum(nums, target)
  hm = Hash.new
  nums.each.with_index do |num, i|
    diff = target - num
    return [hm[diff], i] if hm.nil?
    hm[num] = 1
  end
end
puts two_sum([2,3,4,5], 9)
