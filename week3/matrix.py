class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        rows_to_change = set()
        cols_to_change = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_to_change.add(row)
                    cols_to_change.add(col)


        for row in range(rows):
            for col in range(cols):
                if row in rows_to_change or col in cols_to_change:
                    matrix[row][col] = 0
                    
        