#771. 
#Solution1: faster than 99%
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        
        for s in S:
            if s in J: counter += 1
                    
        return counter
                    
#Solution2: faster than 69%
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        
        for j in J:
            for s in S:
                if s in j: counter += 1
                    
        return counter
                    