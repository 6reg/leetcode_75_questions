def two_sum nums, target = 10
  hm = Hash.new
  nums.each_with_index do |num, index|
    diff = hm[target - num]
    if diff != nil
      return [diff, index]
    else
      hm[num] = index
    end
  end
end

puts two_sum [2,3,4,5,5]
