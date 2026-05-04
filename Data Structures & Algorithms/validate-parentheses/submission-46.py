class Solution:
    def isValid(self, s: str) -> bool:

        val = []

        check = {"]" : "[", "}" : "{", ")" : "("}

        for i in s:
            if i in check:
                if val and val[-1] == check[i]:
                    val.pop()
                else:
                    return False 
        

            else:
                val.append(i)

        return True if not val else False 

            