class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        k = k % len(nums)

        res.extend(nums[-k:])
        res.extend(nums[:-k])

        nums[:] = res 