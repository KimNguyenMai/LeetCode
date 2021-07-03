#20. 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 != 0: return False
        
        for paren in s: 
            if paren == "(" or paren == "[" or paren == "{":
                stack.append(paren)
            elif paren == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            elif paren == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            elif paren == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
                
        if len(stack) != 0: return False 
        else: return True 
                