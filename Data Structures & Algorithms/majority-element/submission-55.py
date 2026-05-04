class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        # return the number with the max count after building the hashmap
        return max(hashmap, key=hashmap.get)