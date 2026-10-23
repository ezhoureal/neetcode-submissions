class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_row = False
        zero_col = False
        for i in range(m):
            for j, cell in enumerate(matrix[i]):
                if cell == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    
                    if i > 0 and j > 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0
        