class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {"]" : "[", ")" : "(", "}" : "{"}

        resolt = []



        for i in s:

            if i in hashmap:
                if resolt and resolt[-1] == hashmap[i]:
                    resolt.pop()
                else:
                    return False 


            
            else:
                resolt.append(i)

        return len(resolt) == 0