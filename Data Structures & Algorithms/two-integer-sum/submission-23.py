class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    
     
        hashmap = {} # build hashmap to map it for a number

        for i, n in enumerate(nums): # for loop with enumrate function to search for number and index 
            diff = target - n # calculate diff number to reach target 

            if diff in hashmap:
                return [hashmap[diff], i]

            else:
                hashmap[n] = i

        return nums