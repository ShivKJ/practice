class Solution:
    def maximalSquare(self, matrix) -> int:
        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                value = int(matrix[i][j])

                if i == 0 or j == 0 or value == 0:
                    matrix[i][j] = value
                else:
                    matrix[i][j] = 1 + min([matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]])

                result = max(result, matrix[i][j])

        return result
