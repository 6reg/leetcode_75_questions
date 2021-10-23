"""
There is always only 1 pair of numbers that satisfy the condition (sum to target). We can assume that for all numbers in the list (x1, x2,..xn), there exists a pair such that xa + xb = target.
To solve with single pass of list (big O of n) we can change equation to
xa = target - xb and since we know the target, as long as we maintain a record of values we can compare current val (xa) to it's only pair, if itexists, in record of all previous values (xb)
dictionary will hold key : value (target-number) : indice
"""

def twoSum(nums, target):
    hashmap = {} # to hold xa : index
    for i in range(len(nums)):
        if nums[i] in hashmap:
            return [hashmap[nums[i]], i] # if num shows up in dict already
                                        # that means necesarry pair has been
                                        # iterated on already
        hashmap[target - nums[i]] = i

print(twoSum([2, 7, 5, 3], 9))
