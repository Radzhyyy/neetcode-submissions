class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        left = 0
        right = number_of_rows * number_of_columns - 1

        while left <= right:
            middle = (left + right) // 2

            row_index = middle // number_of_columns
            column_index = middle % number_of_columns

            if matrix[row_index][column_index] == target:
                return True
            elif matrix[row_index][column_index] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False