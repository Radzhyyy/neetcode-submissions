class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for num in nums:
            if num in mp:
                continue
            left = mp.get(num - 1, 0)
            right = mp.get(num + 1, 0)
            total = left + right + 1
            mp[num] = total
            mp[num - left] = total
            mp[num + right] = total
            res = max(res, total)
        return res