def hm(nums, target)
  hm = {}
  nums.each |num| do
    diff = target - num
    if diff in hm
      return hm[diff], num
    hm[num] = diff
    end
  end
end

puts hm([1,2,4,5], 9)
