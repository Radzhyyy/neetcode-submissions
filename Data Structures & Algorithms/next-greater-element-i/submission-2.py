class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap = {}
        res = []

        for num in nums2:

            while res and res[-1] < num:
                hashmap[res.pop()] = num

            res.append(num)

        return [hashmap.get(i, -1) for i in nums1]