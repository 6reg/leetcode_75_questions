def twoSum(nums, target):
    hm = {}
    for index, value in enumerate(nums):
        diff = target - nums[index]
        if diff in hm:
            return [hm[diff], index]
        hm[value] = index

print(f'{twoSum([2,7,9], 16)}')
