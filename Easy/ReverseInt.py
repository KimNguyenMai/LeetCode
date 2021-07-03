#7. Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        arr = [str (elem) for elem in str(x)]
        
        if arr[0] == '-':
            arr.pop(0)
            while arr[-1] == '0':
                arr.pop()
                reversed = arr [::-1]
            else:
                reversed = arr [::-1]
            reversed.insert(0, '-')
            
        elif arr [-1] == '0':
            if len(arr) ==1:
                result = '0'
            while len(arr) > 1 and arr [-1] == '0': 
                arr.pop()
            reversed = arr [::-1]
            
        else:
            reversed = arr [::-1]
            
        result = ''.join(map(str, reversed))
        
        if int(result) >= -2**31 and int(result) <= 2**31-1: 
            return(int(result))
        else:
            return 0