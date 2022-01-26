def hm(nums, target)
  h = Hash.new
  nums.map.with_index do |num, i|
    diff = num - i
    if h[diff] != nil
      return [diff, i]
    h[diff] = i
    end
  end
end

puts hm([3,4,5,2], 9)
