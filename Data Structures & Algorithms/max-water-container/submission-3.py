class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maX = 0

        while l < r:
            total = (r - l) * min(heights[l], heights[r])
            maX = max(maX, total)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maX
