class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #1. create list ##
        #2. sort the list for two pointer ##
        #3. for loop index and value ##
        #4. if first number > 0 stop the scan we will not get 0 anyway ##
        #5. check for dublicates not to scan next number if the same ##
        #6. Build two pointers ##
        #7. find number = to first num which we looking to get 0 ##
        #8. wirite this 3 numbers to the list and move pointers #
        #9. Skip duplicate values so we don’t repeat triplets. form numbers which we found
        #10 return loop to the list

        nums.sort() # O(n log n)

        res = [] # O(n)

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i -1]:
                continue


            l = i + 1
            r = len(nums) - 1


            while l < r:
                thresum = nums[i] + nums[r] + nums[l]

                if thresum > 0:
                    r -= 1

                elif thresum < 0:
                    l += 1

                else:

                    res.append([nums[i], nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l -1 ] and l < r:
                        l += 1

        return res



