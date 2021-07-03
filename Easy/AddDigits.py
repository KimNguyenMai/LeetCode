#258. Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) != 1:
            num = num // 10 + (num% 10)
        return num