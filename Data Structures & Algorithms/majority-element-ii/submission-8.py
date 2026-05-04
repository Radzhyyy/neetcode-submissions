class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashmap = {}


        for i in range(len(nums)):

            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1


        result = []

        for key, value in hashmap.items():

            if value > len(nums) // 3:
                result.append(key)

        return result
        