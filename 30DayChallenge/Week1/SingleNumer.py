class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
            
        for i in range (len(nums) - 1):
            result ^= i
        return result 