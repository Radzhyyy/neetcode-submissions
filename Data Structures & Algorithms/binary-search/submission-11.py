class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 # left poimter start at 0

        r = len(nums) - 1 # right pointer start -1 index 

        while l <= r: # loop if l pointer less then r pointer 
            m = l + ((r - l) // 2) # calculate middle pointer 
            if nums[m] < target: # if number less them m we can move l + 1
                l = m + 1 # move l pointer to index of m + 1
            
            
            elif nums[m] > target:
                r = m - 1  # if target num less then m we move m 
            else:
                return m

        return - 1
            

