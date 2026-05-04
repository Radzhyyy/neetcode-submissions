class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} # val --> index

        for index, number in enumerate(nums):
            diff = target - number
            if diff in Map:
                return [Map[diff], index]
            
            else:
                Map[number] = index

        