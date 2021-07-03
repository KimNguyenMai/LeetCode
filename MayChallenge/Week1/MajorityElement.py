#Solution 1: 168ms run time, 15.3MB memory usage, beats 89% python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for i in nums:
            if count[i] > len(nums)//2:
                return i

#Solution 2:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        mid = len(nums)//2
        
        for i,j in count.items():
            if j > mid:
                return i