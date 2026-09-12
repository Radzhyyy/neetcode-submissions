class Solution:
    def findMin(self, nums: List[int]) -> int:
            l = 0 
            r = len(nums) - 1
            while l < r:
                m = (r + l) // 2
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
            return nums[l]
#             m l    r
# nums = [3,4,5,6,1,2]