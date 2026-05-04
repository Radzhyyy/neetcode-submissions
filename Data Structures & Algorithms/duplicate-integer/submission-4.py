class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cal = set()

        for i in nums:
            if i in cal:
                return True
            cal.add(i)
        
        return False
