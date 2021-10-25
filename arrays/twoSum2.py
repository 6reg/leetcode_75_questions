"""
Brute force approach. For each ith element, check if target minus jth element is equal to the is equal to ith element. If so, return list with indices i, j.
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]

print(twoSum([2,5,7,11], 12))
