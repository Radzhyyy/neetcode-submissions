class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0

        r = len(nums) -1



        while l <= r:

            M = (r + l) // 2


            if target > nums[M]:

                l = M + 1

            elif target < nums[M]:
                r = M - 1

            else:

                return M

        return -1