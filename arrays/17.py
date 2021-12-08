def twoSum(lst, targ):
    hm={}
    for i, v in enumerate(lst):
        diff = targ - lst[i]
        if diff in hm:
            return [hm[diff], i]
        hm[v] = i

print(twoSum([1, 2, 3], 5))
