class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

    
     
        hashmap = {} # build hashmap to map it for a number

        for i, n in enumerate(numbers): # for loop with enumrate function to search for number and index 
            diff = target - n # calculate diff number to reach target 

            if diff in hashmap:
                return [hashmap[diff], i + 1]

            else:
                hashmap[n] = i + 1

        return numbers