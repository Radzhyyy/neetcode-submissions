class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}



        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1  # count occurrences

        n = len(nums)
        for key, count in hashmap.items():
            if count > n // 2:   # majority element
                return key       # ✅ return the integer