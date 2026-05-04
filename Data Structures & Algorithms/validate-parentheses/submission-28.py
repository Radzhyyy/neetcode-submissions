class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ClosedToOpen = {"}" : "{", "]" : "[", ")" : "("}

        for e in s:
            if e in ClosedToOpen:
                if stack and stack[-1] == ClosedToOpen[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        
        return True if not stack else False 