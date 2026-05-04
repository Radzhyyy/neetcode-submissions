class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        resolt = max(hashmap, key=hashmap.get)


        return resolt