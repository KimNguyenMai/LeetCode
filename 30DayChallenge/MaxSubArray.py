#Kadane Algorithm:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum


#devine and conquer:
# devineArr = len(nums) // 2
#         Left = nums[:devineArr]
#         Right = nums[devineArr + 1:]
        
#         sumLeft = 0
#         for i in range(len(Left):0):
#             sumLeft += Left[i] #+ Left[i+1] 
#         return sumLeft
    
#         sumRight = 0
#         for i in range(len(Right)):
#             sumRight += Right[i]
#         return sumRight
    
#         sumArr = sumLeft + sumRight
        
        #compare 3 sums, largest sum is the answer, 