class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def rows(self) -> list:
        """
        Returns a list with the rows in the matrix
        """
        return self.numbers.split("\n")

    def columns(self) -> list:
        """
        Returns a list with the columns in th ematrix
        """
        columns = []
        i = 0
        while i < len(self.rows()[0]):
            column = ""
            for row in self.rows():
                column += row[i] + " "
            i += 2
            columns.append(column[:-1])
        return columns
