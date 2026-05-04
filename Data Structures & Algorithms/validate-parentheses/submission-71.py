class Solution:
    def isValid(self, s: str) -> bool:
        
        check = []
        hashmap = {"]" : "[", ")" : "(", "}" : "{"}



        for i in s:

            if i in hashmap:
                if check and check[-1] == hashmap[i]:
                    check.pop()

                else:
                    return False 
            
            else:
                check.append(i)
        
        return not check




