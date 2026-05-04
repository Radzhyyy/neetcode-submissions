class Solution:
    def isValid(self, s: str) -> bool:

        check = []

        hashmap = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch in hashmap:  # closing bracket
                if check and check[-1] == hashmap[ch]:
                    check.pop()
                else:
                    return False
            else:
                check.append(ch)

        return not check
