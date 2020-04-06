#26.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  
        Len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[Len] = nums[i]
                Len +=1
        return Len
    
    
       