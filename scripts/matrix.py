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
        return vector_format(single_row)  # O(n)

    def column(self, index) -> list:
        """
        Returns a list with the columns in the matrix
        """
        column = []
        for row in self.rows():
            column.append(int(row[index - 1]))
        return column


def vector_format(string_vector: list) -> list:
    """
    : param: string_vector -> a list of strings
    : Return: vector -> formats the list of strings to return the items as integers
    """
    for i in range(len(string_vector)):
        string_vector[i] = int(string_vector[i])
    return string_vector
