class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        SET = set()



        for i in range(len(nums)):

            if nums[i] in SET:
                return True 

            SET.add(nums[i])

        return False 