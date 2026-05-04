class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)

        # Count frequency
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # Collect elements appearing more than n//3 times
        result = []
        for key, value in hashmap.items():
            if value > n // 3:
                result.append(key)

        return result