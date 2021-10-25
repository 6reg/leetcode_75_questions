"""
brute force approach:
loop through each element x and find if there is another value that equals
to target - x
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

print(twoSum([2, 7, 5, 3], 12))
