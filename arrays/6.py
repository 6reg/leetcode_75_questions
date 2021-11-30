def twoSum(nums, target):
    hm = {}
    for index, value in enumerate(nums):
        diff = target - nums[index]
        if diff in hm:
            return [hm[diff], index]
        hm[value] = index

print(twoSum([0,1,2,3], 5))
