#27. 
#Solution1: Passed all test cases
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        count = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[count] = nums[i]
                count += 1
        
        return count
        

# solution 2:
# Does not pass test case: nums = [3,2,2,3], val = 3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        count = 0
        for i in range(len(nums)):
            if val == nums[i]:
                nums.append(nums.pop(nums.index(nums[i]))) 
                count += 1
        
        return len(nums) - count
        



#solution3 
# Does not pass test case: nums = [0,1,2,2,3,0,4,2], val = 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        for i in nums:
            if val == i:
                nums.remove(i)
        return len(nums)
    