class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:

        res = []
        l = 0

        while l < len(s):
            end = l
            while s[end] != '#':
                end += 1

            length = int(s[l:end])
            l = end + 1
            end = l + length
            res.append(s[l:end])
            l = end

        return res

5#Hello5#World
