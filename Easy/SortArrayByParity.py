#905.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        first = 0
        last = len(A) -1 
        
        while first < last:
            if A[last] % 2 == 0: 
                temp = A[first]
                A[first] = A[last]
                A[last] = temp
            
            if A[first] % 2 == 0: first += 1   
            if A[last] % 2 == 1: last -= 1
                
        return A
        