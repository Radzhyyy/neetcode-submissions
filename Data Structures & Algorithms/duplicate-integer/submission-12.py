class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        SET = set()

        for i in nums:
            if i in SET:
                return True
            SET.add(i)
                
        return False 