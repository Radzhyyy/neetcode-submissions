class Solution:
    def check(self, nums: List[int]) -> bool:
        points = 0


        for i in range(len(nums)):

            if nums[i] > nums[(i + 1) % len(nums)]:
                points += 1

        return points < 2