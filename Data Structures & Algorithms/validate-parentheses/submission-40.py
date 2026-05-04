class Solution:
    def isValid(self, s: str) -> bool:

        LIST = []

        check ={"]" : "[", "}" : "{", ")" : "("}

        for i in s:
            if i in check:
                if LIST and LIST[-1] == check[i]:
                  LIST.pop()

                else:
                    return False 

            else:
                LIST.append(i)

        return True if not LIST else False   