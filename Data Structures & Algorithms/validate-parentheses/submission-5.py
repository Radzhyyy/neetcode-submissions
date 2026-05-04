class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ClosedToOpen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in ClosedToOpen:
                if stack and stack[-1] == ClosedToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack  else False 