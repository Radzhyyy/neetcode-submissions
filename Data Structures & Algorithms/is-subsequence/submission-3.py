class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        
        if len(s) == 0:
            return True
        for r in range(len(t)):
            if s[l] == t[r]:
                l += 1
            
                if l == len(s):
                    return True 
        return False 