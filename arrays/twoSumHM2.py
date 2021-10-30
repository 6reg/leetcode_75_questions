def twoSum(nums, target):
    hm = {}
    for index, num in enumerate(nums):
        diff = target - nums[index]
        if diff in hm:
            return [hm[diff], index]
        hm[num] = index
print(twoSum([2, 7, 9], 9))
