# 1343. 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Given an array of integers arr and two integers k and threshold.
# Return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        summ = sum(arr[:k])
        
        for i in range (len(arr) - k+1):
            if summ >= threshold * k:
                counter += 1        
            if(k+i>=len(arr)):
               break
            summ = summ - arr[i] + arr[i+k]
        return counter
        
        