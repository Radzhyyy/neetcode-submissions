class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        many_row = len(matrix)
        many_cols = len(matrix[0])

        l = 0
        r = many_row * many_cols -1

        while l <= r:
            m = (l + r) // 2

            row_index = m // many_cols
            cols_index = m % many_cols

            if target < matrix[row_index][cols_index]:
                r = m - 1

            elif target > matrix[row_index][cols_index]:
                l = m + 1

            else:
                return True 

        return False 