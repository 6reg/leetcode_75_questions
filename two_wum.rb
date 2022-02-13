def main
  def two_sum nums, target
    hashmap = Hash.new
    nums.each_with_index do |num, index|
      diff = hashmap[target - num]
      return [diff, index] if diff
    hashmap[num] = index
    end
  end
 puts two_sum [2,3,4,5], 9
end

main


