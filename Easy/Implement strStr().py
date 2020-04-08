#28.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        while len(haystack) == 0:
            if len(needle) == 0: return 0
            elif len(needle) != 0: return -1 
        
        while len(haystack) != 0:
            if len(needle) == 0: return 0
            elif needle not in haystack: return -1
            elif len(needle) != 0 and needle in haystack: return haystack.index(needle)
    
        