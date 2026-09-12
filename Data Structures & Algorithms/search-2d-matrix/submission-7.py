class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        how_many_row = len(matrix)
        how_many_cols = len(matrix[0])


        l = 0
        r = how_many_row * how_many_cols - 1

        while l <= r:

            m = (l + r) // 2

            row_index = m // how_many_cols
            cols_index = m % how_many_cols

            if target < matrix[row_index][cols_index]:
                r = m - 1

            elif target > matrix[row_index][cols_index]:
                l = m + 1

            else:
                return True

        return False 