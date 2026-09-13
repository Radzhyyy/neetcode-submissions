class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2


            if nums[m] == target:
                return m

             #left side is sorted            
            if nums[l] <= nums[m]:
                # Is the TARGET inside the sorted left half?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right side is sorted
            else:

                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            


        return -1

#Input: nums = [3,4,5,6,1,2], target = 1
