class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def matrix(self) -> list:
        """
        Returns the matrix formated with each row as a list of string elements
        """
        return [row.split(" ") for row in self.matrix_string.split("\n")]

    def row(self, row_number: int) -> list:
        """
        Returns the row requested by row_number
        """
        single_row = self.matrix()[row_number - 1]
        return [int(single_row[i]) for i in range(len(single_row))]

    def column(self, column_number) -> list:
        """
        Returns a list with the columns in the matrix
        """
        return [int(row[column_number - 1]) for row in self.matrix()]
