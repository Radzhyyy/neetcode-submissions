class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        a = 0


        while w < len(word) and a < len(abbr): # keep 2 pointer inside of the string
   
            if abbr[a].isdigit():
                
                if abbr[a] == "0":
                    return False 
            
                num = 0
                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1

                w += num

            else:
                if word[w] != abbr[a]:
                    return False 

                w += 1
                a += 1

        return w == len(word) and a == len(abbr)


