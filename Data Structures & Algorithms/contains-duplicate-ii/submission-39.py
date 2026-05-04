class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashset = set()
        l = 0


        for i in range(len(nums)):
            
            if i - l > k:
                hashset.remove(nums[l])
                l += 1

           
            if nums[i] in hashset:
                return True

            hashset.add(nums[i])

        return False 


