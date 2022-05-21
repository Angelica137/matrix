class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def rows(self) -> list:
        """
        Returns a list with the rows in the matrix
        """
        rows = self.matrix_string.split("\n")  # O(n)
        matrix = []
        for row in rows:  # O(n)
            matrix.append(row.split(" "))
        return matrix

    def row(self, row_number: int) -> list:
        """
        Returns the row requested by row_number
        """
        single_row = self.rows()[row_number - 1]  # O(n)
        for i in range(len(single_row)):
            single_row[i] = int(single_row[i])
        return single_row

    def column(self, index) -> list:
        """
        Returns a list with the columns in the matrix
        """
        column = []
        for row in self.rows():
            column.append(int(row[index - 1]))
        return column
