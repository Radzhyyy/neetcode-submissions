class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        SET = set(nums)

        res = 0

        for num in nums:
            if (num -1) not in SET:
                count = 0

                while (num + count) in SET:
                    count += 1

                res = max(count, res)


        return res