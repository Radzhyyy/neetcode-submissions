class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}


        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1


        resolt = max(hashmap, key=hashmap.get)

        return resolt        