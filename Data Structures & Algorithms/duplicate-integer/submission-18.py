class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        SET = []

        for i in nums:
            if i in SET:
                return True

            SET.append(i)

        return False 