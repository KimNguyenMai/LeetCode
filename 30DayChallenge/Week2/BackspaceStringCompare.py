#844.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        SCount = 0
        TCount = 0
        
        SPointer = len(S) - 1
        TPointer = len(T) - 1
        
        while SPointer >= 0 or TPointer >= 0:
            while (SPointer >= 0):
                if S[SPointer] == '#':
                    SCount +=1
                    SPointer -=1
                elif SCount > 0:
                    SPointer -= 1
                    SCount -= 1
                else: break

            while (TPointer >= 0):
                if T[TPointer] == '#':
                    TCount +=1
                    TPointer -=1
                elif TCount > 0:
                    TPointer -= 1
                    TCount -= 1
                else: break
                    
            if SPointer >= 0 and TPointer >=0  and S[SPointer] != T[TPointer]: 
                return False
            if (SPointer >=0) != (TPointer >= 0): return False
            
            
            SPointer -= 1
            TPointer -= 1
                
        return True
            