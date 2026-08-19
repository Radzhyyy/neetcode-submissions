class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hashmapS = {}
        hashmapT = {}


        for i in s:
            hashmapS[i] = hashmapS.get(i, 0) + 1

        for i in t:
            hashmapT[i] = hashmapT.get(i, 0) + 1

           
 

        return hashmapS == hashmapT