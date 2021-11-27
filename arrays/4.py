def twoSums(nums, targ):
    hm = {}
    for i, v in enumerate(nums):
        diff = targ - nums[i]
        if diff in hm:
            return [hm[diff], i]
        hm[v] = i
print(twoSums([2, 7, 9], 9))
