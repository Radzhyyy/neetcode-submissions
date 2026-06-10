class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for i in strs:
            res.append(str(len(i)) + "#" + i)

        return "".join(res)
       
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = 0

        while start < len(s):
            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            res.append(s[start:end])
            start = end

        return res
    
5#Hello5#World
