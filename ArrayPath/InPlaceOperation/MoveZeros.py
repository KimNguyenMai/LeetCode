#Solution 1:
for i in nums:
    if i == 0: 
        nums.remove(i)
        nums.append(0)
                
#Solution 2:       
temp = []
for i in nums:
    if i == 0: 
        temp.append(i)
        nums.pop(nums[i])
nums += temp

#Solution 3: 2 pointer