class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        hashsetS = {}

        hashsetT = {}


        for s1, t1 in zip(s, t):

            if hashsetS.get(s1, t1) != t1:
                return False 
            
            if hashsetT.get(t1, s1) != s1:
                return False 

            hashsetS[s1] = t1
            hashsetT[t1] = s1
            

        return True 

