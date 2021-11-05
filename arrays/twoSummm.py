def twoSum(lst, target):
    hm = {}
    for i, n in enumerate(lst):
        diff = target - i
        if diff in hm:
            return [hm[diff], i]
        hm[n] = i

print(twoSum([2, 7, 9], 9))

