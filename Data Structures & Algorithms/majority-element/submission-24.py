class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}


        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1


        resolt = max(hashmap, key=hashmap.get)
        return resolt