class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
            
        for i in range (len(nums) - 1):
            result ^= i
        return result 
    
    
     #while i < len(nums):
            # if base != check: 
            #     nums[check] += 1
            # else: nums[base] += 1