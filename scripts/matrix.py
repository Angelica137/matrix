class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def matrix(self) -> list:
        """
        Returns a list with the rows in the matrix
        """
        matrix = [row.split(" ") for row in self.matrix_string.split("\n")]
        return matrix

    def row(self, row_number: int) -> list:
        """
        Returns the row requested by row_number
        """
        single_row = self.matrix()[row_number - 1]
        single_row = [int(single_row[i]) for i in range(len(single_row))]
        return single_row

    def column(self, column_number) -> list:
        """
        Returns a list with the columns in the matrix
        """
        column = []
        for row in self.matrix():
            column.append(int(row[column_number - 1]))
        return column
