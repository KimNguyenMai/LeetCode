#28.
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? 
# This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        while len(haystack) == 0:
            if len(needle) == 0: return 0
            elif len(needle) != 0: return -1 
        
        while len(haystack) != 0:
            if len(needle) == 0: return 0
            elif needle not in haystack: return -1
            elif len(needle) != 0 and needle in haystack: return haystack.index(needle)
    
      