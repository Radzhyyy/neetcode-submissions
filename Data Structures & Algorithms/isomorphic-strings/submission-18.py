class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        hashmapS = {}

        hashmapT = {}


        for s1, t1 in zip(s, t):

            if hashmapS.get(s1, t1) != t1:
                return False 

            if hashmapT.get(t1, s1) != s1:
                return False 


            hashmapT[t1] = s1
            hashmapS[s1] = t1

        return True 