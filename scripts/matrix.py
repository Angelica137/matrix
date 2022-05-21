class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def rows(self) -> list:
        """
        Returns a list with the rows in the matrix
        """
        rows = self.matrix_string.split("\n")
        matrix = []
        for row in rows:
            matrix.append(row.split(" "))
        return matrix

    def row(self, row_number: int) -> list:
        """
        Returns the row requested by row_number
        """
        single_row = self.rows()[row_number - 1].split(" ")
        return vector_format(single_row)

    def columns(self) -> list:
        """
        Returns a list with the columns in the matrix
        """
        columns = []
        rows = []
        for row in self.rows():
            rows.append(row.split(" "))
        i = 0
        while i < len(rows[0]):
            column = []
            for row in rows:
                column.append(row[i])
            columns.append(column)
            i += 1
        return columns

    def column(self, column_number: int) -> list:
        """
        Returns a list with the column itens for the requested column
        """
        single_column = self.columns()[column_number - 1]
        return vector_format(single_column)


def vector_format(string_vector: list) -> list:
    """
    : param: string_vector -> a list of strings
    : Return: vector -> formats the list of strings to return the items as integers
    """
    for i in range(len(string_vector)):
        string_vector[i] = int(string_vector[i])
    return string_vector
