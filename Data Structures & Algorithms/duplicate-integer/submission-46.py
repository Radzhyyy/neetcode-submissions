class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        SET = set()


        for num in nums:
            if num in SET:
                return True

            SET.add(num)

        return False