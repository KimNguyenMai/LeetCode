# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        
        for i in range (0, len(nums)):
            second = target - nums[i]
            
            if (second in nums and i != nums.index(second)):
                arr.append(i)
                arr.append(nums.index(second))
                            
                return arr
