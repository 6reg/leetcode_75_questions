def hm(nums, target)
  h = Hash.new
  nums.each_with_index do |item, index|
    i = h[target - item]
    return [i, index] if i != nil
    h[item] = index
  end
end

puts hm [5,4,5,3,], 8
  
