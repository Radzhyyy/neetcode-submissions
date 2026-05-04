class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maX = 0


        while l < r:
            resolt = (r - l) * min(heights[l], heights[r])
            maX = max(maX, resolt)

            if heights[l] < heights[r]:
                l += 1
            
            elif heights[r] > heights[l]:
                r -= 1

            else:
                r -= 1

        return maX
