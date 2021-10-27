def twoSum(nums, target): # nums = [2, 7, 9] target = 9
    hashmap={} ## hashmap = { 2 : 0 }
    for index, value in enumerate(nums): # 0:2 ## 1:7 ### 2:9
        diff = target - value # diff = 9 - 2 = 7 ## 9 - 7 = 2
        if diff in hashmap: # index[0]: hashmap empty ## true
            return [hashmap[diff], index] ## [0, 1]
        hashmap[value] = index # hashmap[2] = 0
print(twoSum([2, 7, 9], 9))
