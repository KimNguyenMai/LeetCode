class Solution:
    def next(self, n: int) -> int:
        result = 0
        while n > 0:
            result += (n % 10) * (n %10)
            n /= 10
        return result
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.next(n)
        
        while slow != fast:
            slow = self.next(slow)
            fast = self.next(self.next(fast))
        return slow == 1

#Solution :

class Solution:    
    def isHappy(self, n: int) -> bool:
        count = 0
        while count in range (6):
            toStr = str(n)
            n = 0
            for i in toStr:
                n += int(i)**2
            if n == 1:
                return True
            count += 1
        return False
    