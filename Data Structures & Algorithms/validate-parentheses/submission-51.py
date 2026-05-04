class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {"]" : "[", ")" : "(", "}" : "{"}

        resolt = []


        for i in s:
            if i in hashmap:
                if resolt and resolt[-1] == hashmap.get(i):
                    resolt.pop()

                else:
                    return False
            else:
                resolt.append(i)



        return True if not resolt else False 