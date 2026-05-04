class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # 2 pointers
        # if digit is num
        # if digit is 0
        # build to push word pointer
        # else if 2 pointers not the same 
        # return pointers with same word len

        w = 0
        a = 0

        while w < len(word) and a < len(abbr):

            if abbr[a].isdigit():

                if abbr[a] == '0':
                    return False 


                num = 0

                while a < len(abbr) and abbr[a].isdigit():

                    num = num * 10 + int(abbr[a])

                    a += 1
                w += num

            else:

                if word[w] != abbr[a]:
                    return False

                else:
                    w += 1
                    a += 1
        return a == len(abbr) and w == len(word)
                


