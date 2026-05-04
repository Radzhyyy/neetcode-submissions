class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        hashmap = {}


        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        total = hashmap.get(target, 0)
        return total > len(nums) // 2
        