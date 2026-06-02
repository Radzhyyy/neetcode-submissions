class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}" : "{", ")" : "(", "]" : "["}

        res = []

        for i in s:
            if i in hashmap:
                if res and res[-1] == hashmap.get(i):
                    res.pop()

                else:
                    return False 

            else:
                res.append(i)

        return not res



   
