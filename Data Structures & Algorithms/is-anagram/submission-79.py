class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashsetS = {}
        hashsetT = {}


        for i in range(len(s)):
            hashsetS[s[i]] = hashsetS.get(s[i], 0) + 1
        for i in range(len(t)):
            hashsetT[t[i]] = hashsetT.get(t[i], 0) + 1

        if hashsetS == hashsetT:
            return True

        return False 