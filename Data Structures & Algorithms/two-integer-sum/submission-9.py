class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in check:
                return [check[diff], i]

            check[n] = i