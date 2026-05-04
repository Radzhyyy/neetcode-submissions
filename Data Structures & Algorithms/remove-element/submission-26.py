class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        res = []
        for r in range(len(nums)):

            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l



   