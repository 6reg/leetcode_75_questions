def twoSum(nums, target):
    dic = {}
    for i, v in enumerate(nums):
        diff = target - nums[i]
        if diff in dic:
            return [dic[diff], i]
        dic[v] = i

print(twoSum([2,7,9],9))
