# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

#Solution 1(92ms runtime, O(N)):
class Solution:
    def firstUniqChar(self, s: str) -> int: 
        count = Counter(s)
        
        for i, c in enumerate(s):
            if count[c] == 1: 
                return i
        return -1

#Solution 2 (5380ms runtime)
class Solution:
    def firstUniqChar(self, s: str) -> int:                
        for i, c in enumerate(s):
            counter = s.count(c)
            if counter == 1: 
                return i
        return -1