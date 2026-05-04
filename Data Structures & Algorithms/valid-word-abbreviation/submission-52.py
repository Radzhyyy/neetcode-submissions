class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = 0
        w = 0

        while a < len(abbr) and w < len(word):

            if abbr[a].isalpha():
                if abbr[a] != word[w]:
                    return False 
                
                w += 1
                a += 1

            elif abbr[a] == '0':
                return False 


            else:

                num = 0

                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1

                w += num

        return a == len(abbr) and w == len(word)
  


