class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 0

                while (num + count) in numSet:
                    count += 1

                ans = max(ans, count)

        return ans



#2,20,4,10,3,4,5