def twoSum(nums, target):
    d={}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n]=i

print(twoSum([2,7,9], 9))

