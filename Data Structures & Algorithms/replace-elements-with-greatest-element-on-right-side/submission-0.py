class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMAX = -1

        for i in range(len(arr)-1, -1, -1):
            newMAX = max(rightMAX, arr[i])
            arr[i] = rightMAX
            rightMAX = newMAX
        return arr

