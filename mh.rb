def hm(nums, target)
  h = Hash.new
  nums.each.with_index do |num, i|
    diff = target - num
    return [h[diff], i] if h[diff] != nil
  h[num] = i 
 end
end

mike = hm([1,2,3,4,5], 9)
puts mike.join(" ")
