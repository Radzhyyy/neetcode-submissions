class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1



        while l <= r:

            M = (r + l) // 2


            if nums[M] < target:
                l = M + 1

            
            elif nums[M] > target:
                r = M - 1

            else:
                return M

        return -1
