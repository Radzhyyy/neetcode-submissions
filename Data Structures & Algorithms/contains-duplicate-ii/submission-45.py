class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

   
        l = 0

        hashset = set()


        for i in range(len(nums)):
            
            if l + i > k:
                hashset.remove(nums[l])
                l += 1

            if nums[i] in hashset:
                return True

            hashset.add(nums[i])
            
        return False 
        