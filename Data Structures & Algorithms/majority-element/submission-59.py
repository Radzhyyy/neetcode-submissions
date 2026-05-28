class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ans = {}

        for i in range(len(nums)):
            ans[nums[i]] = ans.get(nums[i], 0) + 1

        return max(ans, key=ans.get)