# 9. Palindrome Number

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?


#Solution1. Turn to a string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]

        if y == str(x):
            return True
        else:
            return False


#Solution 2. reverse int
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x
        
        while x > 0:
            remainder = x % 10
            reverse =  (reverse * 10) + remainder
            x = x // 10
            
        if x == reverse or temp == reverse:
            return True
        else:
            return False

#Solution 3. Two pointer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        first= 0
        last =len(str(x))-1
        
        while first < last:
            if(str(x)[first]!=str(x)[last]):
                return False
            else:
                first=first+1
                last=last-1
        return True