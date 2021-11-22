def twoSum(nums, target):
    hm = {} # create empty dict to store
    for index, value in enumerate(nums):
        diff = target - nums[index]
        if diff in hm:
            return [hm[diff], index]
        hm[value] = index

print(twoSum([2,7,9], 9))
