"""
This program takes a list of numbers and a target number and returns
the indices of the numbers in the list that add up to the target number.
"""

nums=[2,7,9,11]
target=20

def twoSum(nums,target):
    hashmap={}
    for i, j in enumerate(nums):
        diff = target - j
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[j] = i

print(twoSum(nums,target))
