def twoSum(nums, target):
    hm = {}
    for i, v in enumerate(nums):
        diff = target - nums[i]
        if diff in hm:
            return [hm[diff], i]
        hm[v] = i
print(twoSum([5,6,12,2,14], 16))
