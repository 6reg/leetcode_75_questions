class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for num in range(len(nums)):
            if num in hm:
                return [hm[num], hm[num+1]]
        hm[num] = num
        
print(twoSum([2,7,9], 9))    
