def twoSum(nums, target):
    for i in range(len(nums)):
        for y in range(i+1, len(nums)):
            if nums[y] == target - nums[i]:
                return [i, y]

print(twoSum([2,4,6,9], 10))
