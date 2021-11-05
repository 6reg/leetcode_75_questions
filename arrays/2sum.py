def twoSum(lst, target):
    hm = {}
    for i, v in enumerate(lst):
        diff = target - lst[i]
        if diff in hm:
            return [hm[v], i]
        hm[i] = diff

print(twoSum([2, 7, 9], 9))
