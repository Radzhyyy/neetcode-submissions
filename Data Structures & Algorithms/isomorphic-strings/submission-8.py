class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST = {}
        mapTS = {}



        for s1, t2 in zip(s, t):

            if mapST.get(s1, t2) != t2:
                return False 

            if mapTS.get(t2, s1) != s1:
                return False 


            mapST[s1] = t2
            mapTS[t2] = s1

        return True 