class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        w = 0

        a = 0


        while a < len(abbr) and w < len(word):
            if abbr[a].isalpha():
                if abbr[a] != word[w]:
                    return False
                a += 1
                w += 1
            elif abbr[a] == '0':
                return False 

            else:

                num = 0
                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1

                w += num


        return a == len(abbr) and w == len(word)
